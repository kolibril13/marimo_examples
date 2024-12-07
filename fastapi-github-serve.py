# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "fastapi",
#     "marimo",
#     "starlette",
#     "requests",
#     "pydantic",
#     "jinja2",
# ]
# ///


# based on https://github.com/marimo-team/marimo/blob/f2c288b7dfd3d07cf4b7dd298d1ef0166eea6f4b/examples/frameworks/fastapi-github/main.py

import tempfile
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import marimo
import os
import logging
import requests
from pathlib import Path
from jinja2 import Template

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
GITHUB_REPO = os.environ.get("GITHUB_REPO", "marimo-team/marimo")
ROOT_DIR = os.environ.get("ROOT_DIR", "examples/ui")

# Inline HTML Template
HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body class="bg-gray-100">
    <div class="container mx-auto px-4 py-8">
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-3xl font-bold">Welcome, these apps are loaded dynamically from a GitHub repository!</h1>
      </div>
      <h2 class="text-2xl font-semibold mb-4">Available Applications:</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {% for app_name in app_names %}
        <a href="/{{ app_name }}" class="block" target="{{ app_name }}">
          <div class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-4">
            <h3 class="text-lg font-semibold text-blue-600 hover:text-blue-800">{{ app_name }}</h3>
            <p class="text-gray-600 mt-2">Click to open application</p>
          </div>
        </a>
        {% endfor %}
      </div>
    </div>
  </body>
</html>
"""

def download_github_files(repo: str, path: str = "") -> list[tuple[str, str]]:
    """Download files from GitHub repo, returns list of (file_path, content)"""
    api_url = f"https://api.github.com/repos/{repo}/contents/{path}"
    response = requests.get(api_url)
    response.raise_for_status()

    files: list[tuple[str, str]] = []
    for item in response.json():
        logger.debug(f"Processing item: {item}")
        if item["type"] == "file" and item["name"].endswith(".py"):
            content_response = requests.get(item["download_url"])
            content_response.raise_for_status()
            files.append(
                (os.path.join(path, item["name"]), content_response.text)
            )
            logger.debug(f"Downloaded file: {item['name']}")
        elif item["type"] == "dir":
            logger.debug(f"Entering directory: {item['name']}")
            files.extend(
                download_github_files(repo, os.path.join(path, item["name"]))
            )
    return files

tmp_dir = tempfile.TemporaryDirectory()

def setup_apps():
    """Download and setup marimo apps from GitHub"""
    files = download_github_files(GITHUB_REPO, ROOT_DIR)
    server = marimo.create_asgi_app()
    app_names: list[str] = []

    for file_path, content in files:
        app_name = Path(file_path).stem
        local_path = Path(tmp_dir.name) / file_path

        # Create directories if they don't exist
        local_path.parent.mkdir(parents=True, exist_ok=True)

        # Write file content
        local_path.write_text(content)
        logger.debug(f"Wrote content to {local_path}")

        # Add to marimo server
        server = server.with_app(path=f"/{app_name}", root=str(local_path))
        app_names.append(app_name)
        logger.info(f"Added app: {app_name} from {file_path}")

    return server, app_names

# Create a FastAPI app
app = FastAPI()

# Setup marimo apps
server, app_names = setup_apps()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page with available applications."""
    template = Template(HOME_HTML)
    rendered_html = template.render(app_names=app_names, request=request)
    return HTMLResponse(content=rendered_html)

@app.get("/ping")
async def ping():
    """Health check endpoint."""
    return {"message": "pong"}

# Mount the marimo server
app.mount("/", server.build())

# Run the server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000, log_level="info")