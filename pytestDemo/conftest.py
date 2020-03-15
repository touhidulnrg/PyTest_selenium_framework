# fixtures are used as setup and tear down methods for test cases - conftest file to generalize.
# fixture and make it available to all test cases

import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executed first")
    yield
    print("i will executed last")


def dataload():
    print("user profile data is being created.")
    return ['arish', 'islam', 'arish@gmail.com']