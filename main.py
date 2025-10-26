from github_api_module import get_user_data, get_all_repos
from report_generator import create_pdf

if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip()
    profile = get_user_data(username)
    repos = get_all_repos(username)
    create_pdf(username, profile, repos)