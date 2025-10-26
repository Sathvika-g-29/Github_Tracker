# report_generator.py

import requests
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from datetime import datetime
import time
import os

# -----------------------------
# GitHub API helper
# -----------------------------
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "").strip()
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

def get_last_commit(username, repo_name):
    """
    Safely fetch the last commit date for a repository.
    Returns a formatted string or "-" if unavailable.
    """
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    for i in range(3):  # try 3 times
        try:
            r = requests.get(url, headers=HEADERS, params={"per_page": 1}, timeout=5)
            data = r.json()
            if isinstance(data, list) and data:
                dt = data[0]["commit"]["committer"]["date"]
                dt_obj = datetime.fromisoformat(dt.replace("Z", "+00:00"))
                return dt_obj.strftime("%Y-%m-%d %H:%M UTC")
            return "-"
        except Exception:
            time.sleep(1)  # wait 1 sec and retry
    return "-"

# -----------------------------
# PDF generation
# -----------------------------
def create_pdf(username, profile, repos):
    """
    Generate PDF report for a GitHub user.
    """
    os.makedirs("reports", exist_ok=True)
    out_file = os.path.join("reports", f"{username}_github_report.pdf")
    
    c = canvas.Canvas(out_file, pagesize=A4)
    width, height = A4
    margin = 20 * mm
    y = height - margin

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y, f"GitHub Activity Report — {username}")
    y -= 10 * mm

    # Profile info
    c.setFont("Helvetica", 11)
    c.drawString(margin, y, f"Generated on: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    y -= 6 * mm

    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y, "Profile")
    y -= 6 * mm
    c.setFont("Helvetica", 10)

    if profile:
        lines = [
            f"Name: {profile.get('name') or '-'}",
            f"Public Repos: {profile.get('public_repos', 0)}",
            f"Followers: {profile.get('followers', 0)}",
        ]
        for line in lines:
            c.drawString(margin, y, line)
            y -= 5 * mm
    else:
        c.drawString(margin, y, "User not found or no public data available.")
        y -= 6 * mm

    y -= 4 * mm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y, "Repositories (top results)")
    y -= 6 * mm
    c.setFont("Helvetica", 10)

    # Table header
    c.drawString(margin, y, "Name")
    c.drawString(margin + 80 * mm, y, "Last Commit")
    y -= 5 * mm

    for repo in repos:
        if y < margin + 50:
            c.showPage()
            y = height - margin
        repo_name = repo.get("name")
        last_commit = get_last_commit(username, repo_name)
        c.drawString(margin, y, repo_name)
        c.drawString(margin + 80 * mm, y, last_commit)
        y -= 6 * mm

    # Footer
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(margin, 10 * mm, "This report includes public repository data.")
    c.save()
    print(f"PDF saved: {out_file}")