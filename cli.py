from ghub import GHub
from rich.prompt import Prompt
from rich import print
import httpx
import os


def main():
    if not os.environ.get("GITHUB_TOKEN"):
        raise Exception("Please set GITHUB_TOKEN")
    user_name = Prompt.ask("Username?")
    gh = GHub()
    success = gh.load_user(user_name=user_name)
    if success:
        print(gh.repos_table())


if __name__ == "__main__":
    main()
