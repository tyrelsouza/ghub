import httpx


class API:
    headers = {"Accept": "application/vnd.github.v3+json"}

    def __init__(self, user_name: str) -> None:
        self.user = self.load_user(user_name)
        self.user_name = self.user["login"]
        self.repos = self.load_repos()  # TODO: Check if pagination

    def _get(self, url: str) -> dict:
        """Uses httpx.Client().get to send the appropriate github headers, and return the url"""
        with httpx.Client(headers=self.headers) as client:
            return client.get(url).json()

    def _get_paged(self, url: str) -> list:
        """Uses httpx.Client().get to send the appropriate github headers, and return the url"""
        content = []
        with httpx.Client(headers=self.headers) as client:
            while True:
                resp = client.get(url)
                content.extend(resp.json())
                if not resp.links.get('next'):
                    break
                url = resp.links['next']['url']
        return content


    def load_user(self, user_name: str) -> dict:
        """Sets the user object"""
        return self._get(f"https://api.github.com/users/{user_name}")

    def load_repo(self, repo_name: str) -> dict:
        """Set the repo object"""
        return self._get(f"https://api.github.com/repos/{self.user_name}/{repo_name}")

    def load_repos(self) -> dict:
        """Set the users repos"""
        return self._get_paged(f"https://api.github.com/users/{self.user_name}/repos")
