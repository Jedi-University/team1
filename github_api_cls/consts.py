
from decouple import config


FILE_DB_NAME = "top_repos.sqlite"
DB_PATH = f"sqlite:///db/{FILE_DB_NAME}"
GITHUB_TOKEN = config("github_token", default="")
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}