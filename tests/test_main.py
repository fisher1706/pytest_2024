# https://www.youtube.com/watch?v=zc138SwDsG0&list=PLeLN0qH0-mCVdHgdjlnKTl4jKuJgCK-4b&index=9
import pytest
from src.config import settings

# TODO: 1 - use "pytest.ini" - env_files = test.env or command: pytest --envfile .test.env - use: pytest-dotenv


@pytest.fixture(
    scope="session",
    autouse=True
)
def setup_db():
    print(f"\n{settings.MODE}")
    return "text_one"


class TestSomething:
    def test_something(self):
        assert True
