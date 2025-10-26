import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from time import sleep

# Load GitHub token from .env
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

# -----------------------------
# Fetch user profile info
# -----------------------------
def get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    r = requests.get(url, headers=HEADERS)
    return r.json()

# -----------------------------
# Fetch all repositories with pagination
# -----------------------------
def get_all_repos(username):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos"
        r = requests.get(url, headers=HEADERS, params={"per_page": 100, "page": page, "sort": "updated"})
        data = r.json()
        if not data:
            break
        repos.extend(data)
        page += 1
        sleep(0.1)  # be polite to API
    return repos

# -----------------------------
# Get last commit date for a repo
# -----------------------------
def get_last_commit(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    r = requests.get(url, headers=HEADERS, params={"per_page": 1})
    data = r.json()
    if isinstance(data, list) and data:
        dt = data[0]["commit"]["committer"]["date"]
        dt_obj = datetime.fromisoformat(dt.replace("Z", "+00:00"))
        return dt_obj.strftime("%Y-%m-%d %H:%M UTC")
    return "-"