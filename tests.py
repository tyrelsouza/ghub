import json
import pytest
from cli import GHub
from pytest_httpx import HTTPXMock

def _load_user():
    with open("tests/user.json", "r") as f:
        return json.loads(f.read())

def _load_repo():
    with open("tests/repo.json", "r") as f:
        return json.loads(f.read())

def test_user(httpx_mock: HTTPXMock):
    httpx_mock.add_response(method="GET", json=_load_user())

    gh = GHub(user_name="tyrelsouza", repo_name="work_sample")
    gh.set_user()
    assert(gh.user["login"] == "tyrelsouza")

def test_repo(httpx_mock: HTTPXMock):
    httpx_mock.add_response(method="GET", json=_load_repo())

    gh = GHub(user_name="tyrelsouza", repo_name="work_sample")
    gh.set_repo()
    breakpoint()
    assert(gh.repo["login"] == "tyrelsouza2")
    
    
