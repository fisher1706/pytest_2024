import pytest
# from src.config import settings

# TODO: 1 - use "pytest.ini" - env_files = test.env or command: pytest --envfile .test.env - use: pytest-dotenv


# @pytest.fixture(
#     scope="session",
#     autouse=True
# )
# def setup_db():
#     print(f"\n{settings.MODE}")
#     return "text_one"


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         default="chrome",
#         choices=("chrome", "firefox")
#     )


def pytest_addoption(parser):
    parser.addoption(
        "--run-slow",
        default=True,
        choices=("True", "False")
    )
