from fastapi import FastAPI, Request
from pydantic import BaseModel
from github_utils import fetch_python_files
from openai_utils import summarize_code
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allow frontend (like Streamlit) to call this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later restrict this
    allow_methods=["*"],
    allow_headers=["*"],
)

class RepoRequest(BaseModel):
    repo_url: str

@app.post("/analyze")
async def analyze_repo(data: RepoRequest):
    """
    Given a GitHub URL, fetch Python files and summarize each.
    """
    repo_url = data.repo_url
    files = fetch_python_files(repo_url)
    results = {}

    for filename, code in files.items():
        summary = summarize_code(code)
        results[filename] = {
            "summary": summary,
            "preview": code[:300]  # Optional
        }

    return results
