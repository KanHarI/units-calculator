import pytest


def test_passes():
    assert 1 == 1


@pytest.mark.xfail
def test_fails():
    assert 0 == 1
