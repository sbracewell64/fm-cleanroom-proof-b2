from fmproof import parse
import pytest


def test_parse_full():
    d = parse("1.2.3-alpha.1+build.5")
    assert d == {"major": 1, "minor": 2, "patch": 3,
                 "prerelease": "alpha.1", "build": "build.5"}


def test_parse_rejects_garbage():
    with pytest.raises(ValueError):
        parse("1.2")
