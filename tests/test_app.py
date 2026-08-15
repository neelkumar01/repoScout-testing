import os

from app.config import parse_timeout
from app.parser import parse_tags
from app.cache import (
    get_user,
    save_user,
    delete_user,
)
from app.runtime import service_mode


def test_default_timeout():
    assert parse_timeout(None) == 30


def test_normal_timeout():
    assert parse_timeout("10") == 10


def test_parse_tags():
    assert parse_tags(
        "python, github, ai"
    ) == [
        "python",
        "github",
        "ai",
    ]


def test_cache_save():
    save_user(
        "42",
        "Alice",
    )

    assert get_user("42") == "Alice"


def test_cache_delete():
    save_user(
        "99",
        "Bob",
    )

    delete_user("99")

    assert get_user("99") is None


def test_ci_service_mode():

    if os.getenv("GITHUB_ACTIONS") == "true":
        assert service_mode() == "production"