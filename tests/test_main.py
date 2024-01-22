# https://www.youtube.com/watch?v=OIvZ0oHl7rA&list=PLeLN0qH0-mCVdHgdjlnKTl4jKuJgCK-4b&index=7

import pytest
from src.main import Calculator


@pytest.fixture()
def fixture_one():
    print("\ntext_one")
    return "text_one"


@pytest.fixture()
def fixture_two():
    print("\ntext_two")
    return "text_two"


@pytest.mark.usefixtures("fixture_one", "fixture_two")
class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 2, 0.5),
        ]
    )
    def test_divide(self, x, y, res):
        assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 1, 2),
            (5, -1, 4)
        ]
    )
    def test_add(self, x, y, res):
        assert Calculator().add(x, y) == res
