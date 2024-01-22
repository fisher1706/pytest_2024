# https://www.youtube.com/watch?v=oIO7TFHpWyo&list=PLeLN0qH0-mCVdHgdjlnKTl4jKuJgCK-4b&index=6

import pytest
from src.main import Calculator
from contextlib import nullcontext as does_not_rise

# TODO: for test "Exceptions" use "expectation" or "raises"


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 0.5, does_not_rise()),
            (5, -1, -5, does_not_rise()),
            (5, "-1", -5, pytest.raises(TypeError)),
            (5, 0, -5, pytest.raises(ZeroDivisionError))
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
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

    @pytest.mark.parametrize(
        "x, y, res",
        [
            (1, "1", 2)
        ]
    )
    def test_add_with_type_error(self, x, y, res):
        with pytest.raises(TypeError):
            assert Calculator().add(x, y) == res
