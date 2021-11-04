import json
import pytest
from ghub import GHub

def _load_user():
    with open("./tests/fixtures/user.json", "r") as f:
        return json.loads(f.read())

def _load_repos():
    with open("./tests/fixtures/repos.json", "r") as f:
        return json.loads(f.read())

def _fake_tyrel() -> GHub:
    gh = GHub()
    gh.user = _load_user()
    gh.repos = _load_repos()
    return gh


def test_load_repos():
    gh = _fake_tyrel()
    assert gh.repos[0]["git_url"] == "git://github.com/tyrelsouza/genealogy.git"
