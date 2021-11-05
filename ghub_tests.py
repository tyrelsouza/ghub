import json
import pytest
from ghub import GHub
from pytest_httpx import HTTPXMock

def _load_fixture(name: str):
    with open(f"./tests/fixtures/{name}.json", "r") as f:
        return json.loads(f.read())

def _fake_tyrel() -> GHub:
    gh = GHub()
    gh.user = _load_fixture("user")
    gh.repos = _load_fixture("repos_1")
    return gh


def test_load_repos():
    gh = _fake_tyrel()
    assert gh.repos[0]["git_url"] == "git://github.com/tyrelsouza/genealogy.git"

def test_repos_trimmed():
    gh = _fake_tyrel()
    repos = list(gh.repos_trimmed())
    assert repos[0] == ['genealogy', 'None', '0','0','0', '0']


def test_get(httpx_mock: HTTPXMock):
    httpx_mock.add_response(method="GET", json=_load_fixture("user"))
    httpx_mock.add_response(method="GET", json=_load_fixture("repos_1"))
    gh = GHub()
    gh.load_user('tyrelsouza')
    assert gh.user["login"] == "tyrelsouza"
    assert len(gh.repos) == 1

def test_table():
    gh = _fake_tyrel()
    table = gh.repos_table()
    assert table.row_count == 1
    assert table.columns[0]._cells[0] == 'genealogy'
    assert table.columns[1]._cells[0] == 'None'
    assert table.columns[2]._cells[0] == '0'
    assert table.columns[3]._cells[0] == '0'
    assert table.columns[4]._cells[0] == '0'

