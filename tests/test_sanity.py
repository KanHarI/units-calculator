import pytest


def test_passes() -> None:
    assert 1 == 1


@pytest.mark.xfail
def test_fails() -> None:
    assert 0 == 1  # type: ignore
