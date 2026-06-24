import pytest
from app.utils import some_utility_function


def test_some_utility_function():
    result = some_utility_function(arg1, arg2)
    assert result == expected_result