import pytest
from src.processing import filter_by_state, sort_by_date, original_state


def test_filter_by_state(test_original_state):
    assert filter_by_state(original_state, state_id=test_original_state)


def test_filter_by_state_1(test_original_state_1):
    assert filter_by_state(original_state) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

def test_filter_by_state_sort(test_original_state_1):
    assert sort_by_date(original_state) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]