# https://www.youtube.com/watch?v=jsrxqoVasyw&list=PLeLN0qH0-mCVdHgdjlnKTl4jKuJgCK-4b&index=11

# TODO: pytest --browser=firefox - use addoption or pytesr --run-slow=True

import time

import pytest


class TestSomething:
    def test_something(self):
        assert True


# def test_one(browser):
#     print(f"\n{browser}")


@pytest.mark.skipif('config.getoption("--run-slow") == "False"')
def test_slow():
    time.sleep(3)
    print("\nslow test")


def test_one():
    print("\ntest_one")
    time.sleep()


def test_two():
    print("\ntest_two")
    time.sleep(4)
