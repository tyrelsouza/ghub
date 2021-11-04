from rich.table import Table
from rich.prompt import Prompt
from rich import print
from api import API


class GHub:
    user = None
    repos = None

    def load_user(self, user_name: str) -> None:
        self.user_name = user_name
        self.api = API(self.user_name)
        self.user = self.api.user
        self.repos = self.api.repos

    def repos_trimmed(self) -> list:
        for repo in self.repos:
            yield [
                str(f)
                for f in [
                    repo["name"],
                    repo["description"],
                    repo["stargazers_count"],
                    repo["watchers_count"],
                    repo["forks_count"],
                    repo["open_issues_count"],
                ]
            ]

    def repos_table(self) -> Table:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name")
        table.add_column("Description")
        table.add_column("Stargazers")
        table.add_column("Watchers")
        table.add_column("Forks")
        table.add_column("Open Issues")
        for repo in self.repos_trimmed():
            table.add_row(*repo)
        return table
