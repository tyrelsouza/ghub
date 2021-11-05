from ghub import GHub
from rich.prompt import Prompt
from rich import print
import httpx


def main():
    user_name = Prompt.ask("Username?")
    gh = GHub()
    success = gh.load_user(user_name=user_name)
    if success:
        print(gh.repos_table())





if __name__ == "__main__":
    main()
