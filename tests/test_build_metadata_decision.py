"""The build-metadata precedence decision is pending a Browser Sol ruling.

Until the ruling is consumed, the behavior is deliberately unresolved; this test
documents that as a pending decision rather than asserting an unratified choice.
"""
import pytest
from fmproof import compare


@pytest.mark.xfail(reason="build-metadata precedence decision pending fm-sol-control/v2 ruling",
                   raises=NotImplementedError, strict=True)
def test_build_metadata_precedence_decided():
    compare("1.0.0+a", "1.0.0+b")
