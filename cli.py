import httpx
from pprint import pprint


class GHub:
    headers = {"Accept": "application/vnd.github.v3+json"}

    def __init__(self, user_name: str, repo_name: str):
        self.user_name = user_name
        self.repo_name = repo_name

    def get(self, url: str) -> dict:
        """Uses httpx.Client().get to send the appropriate github headers, and return the url"""
        with httpx.Client(headers=self.headers) as client:
            return client.get(url).json()

    def schema(self) -> dict:
        """Show all the schema that are available"""
        return self.get("https://api.github.com")

    def set_user(self):
        self.user = self.get_user()

    def get_user(self) -> dict:
        """Get the user object"""
        return self.get(f"https://api.github.com/users/{self.user_name}")

    def set_repo(self):
        self.repo = self.get_repo()

    def get_repo(self) -> dict:
        """Get the repo object"""
        return self.get(f"https://api.github.com/repos/{self.user_name}/{self.repo_name}")


def main():
    gh = GHub(user_name="tyrelsouza", repo_name="work_sample")
    # pprint(gh.schema())
    pprint(
        (
            gh.get_user(),
            gh.get_repo(),
        )
    )


if __name__ == "__main__":
    main()
