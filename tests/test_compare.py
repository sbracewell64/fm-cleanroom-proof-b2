from fmproof import compare


def test_core_precedence():
    assert compare("1.0.0", "2.0.0") == -1
    assert compare("2.0.0", "2.0.0") == 0


def test_prerelease_below_release():
    assert compare("1.0.0-alpha", "1.0.0") == -1


def test_build_metadata_ignored_in_precedence():
    # Ruled Option A (SemVer 2.0.0 s10): build metadata is ignored for precedence.
    assert compare("1.0.0+a", "1.0.0+b") == 0
