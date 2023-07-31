from unittest.mock import Mock
from lib.time_error import TimeError
import pytest

"""
Test the difference in time
return
"""

def test_error_difference_between_times():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {'unixtime': 1690808426}
    timer_mock = Mock()
    timer_mock.time.return_value = 1690808426.5
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == -0.5
