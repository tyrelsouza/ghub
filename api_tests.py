import json
import pytest
from api import API
from pytest_httpx import HTTPXMock


def _load_user():
    with open("./tests/fixtures/user.json", "r") as f:
        return json.loads(f.read())


def _load_repos():
    with open("./tests/fixtures/repos.json", "r") as f:
        return json.loads(f.read())


def test_load_user(httpx_mock: HTTPXMock):
    httpx_mock.add_response(method="GET", json=_load_user())

    gh = API(user_name="tyrelsouza")
    assert gh.user["login"] == "tyrelsouza"

def test_load_repos(httpx_mock: HTTPXMock):
    httpx_mock.add_response(method="GET", json=_load_user())
    httpx_mock.add_response(method="GET", json=_load_repos())

    gh = API(user_name="tyrelsouza")
    assert gh.repos[0]["git_url"] == "git://github.com/tyrelsouza/genealogy.git"
