import requests

def fetch_python_files(repo_url: str) -> dict:
    """
    Extracts all .py files from the GitHub repo.
    Returns a dict of {filename: code}.
    """
    # Example: https://github.com/psf/requests
    repo_path = repo_url.replace("https://github.com/", "")
    api_url = f"https://api.github.com/repos/{repo_path}/contents"

    response = requests.get(api_url)
    if response.status_code != 200:
        return {}

    files = response.json()
    python_files = {}

    for file in files:
        if file['name'].endswith('.py') and file['type'] == 'file':
            code = requests.get(file['download_url']).text
            python_files[file['name']] = code

    return python_files
