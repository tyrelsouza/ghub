import json
import pytest
import httpx

from api import API
from pytest_httpx import HTTPXMock

LINK1 = '<https://api.github.com/user/6292/repos?page=2>; rel="next", <https://api.github.com/user/6292/repos?page=2>; rel="last"'
LINK2 = '<https://api.github.com/user/6292/repos?page=1>; rel="prev", <https://api.github.com/user/6292/repos?page=2>; rel="last"'


def _load_fixture(name: str):
    with open(f"./tests/fixtures/{name}.json", "r") as f:
        return json.loads(f.read())


def test_except(httpx_mock: HTTPXMock):
    httpx_mock.add_response(method="GET", status_code=403)
    with pytest.raises(httpx.HTTPStatusError):
        API().get("boooger")


def test_get(httpx_mock: HTTPXMock):
    httpx_mock.add_response(method="GET", json=_load_fixture("user"))
    api = API()
    assert api.get("users")["login"] == "tyrelsouza"


def test_get_with_pagination(httpx_mock: HTTPXMock):
    api = API()
    # link, so multiple pages
    httpx_mock.add_response(
        method="GET", json=_load_fixture("repos_1"), headers={"link": LINK1}
    )
    httpx_mock.add_response(
        method="GET", json=_load_fixture("repos_2"), headers={"link": LINK2}
    )

    repos = api.get_with_pagination("repos")
    assert len(repos) == 2

    # No link, so no 2nd page, only one item
    httpx_mock.add_response(method="GET", json=_load_fixture("repos_1"))
    repos = api.get_with_pagination("repos")
    assert len(repos) == 1

    # test exit on dict
    httpx_mock.add_response(method="GET", json=_load_fixture("user"))
    user = api.get_with_pagination("user")
    assert user["login"] == "tyrelsouza"
