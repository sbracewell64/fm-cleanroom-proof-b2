from fmproof import compare
import pytest


def test_core_precedence():
    assert compare("1.0.0", "2.0.0") == -1
    assert compare("2.0.0", "2.0.0") == 0


def test_prerelease_below_release():
    assert compare("1.0.0-alpha", "1.0.0") == -1


def test_build_metadata_is_unresolved():
    with pytest.raises(NotImplementedError):
        compare("1.0.0+a", "1.0.0+b")
