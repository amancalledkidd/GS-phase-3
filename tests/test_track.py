from lib.track import Track
from unittest.mock import Mock

"""
create instance of class
check matches title and artist
"""

def test_matches_title_and_contents():
    tune = Track('Hello', 'Kano')
    assert tune.matches('Kano') == True
    assert tune.matches('Hello') == True

"""
create instance
check matches title and artist
only part of name as input
"""

def test_matches_partial_title_and_contents():
    tune = Track('Who said Hello', ' The Kano OG')
    assert tune.matches('Kano') == True
    assert tune.matches('Hello') == True