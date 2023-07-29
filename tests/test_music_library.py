from lib.music_library import MusicLibrary
from unittest.mock import Mock

""" 
test add by adding two tracks
search for one track
return track in list
use mock classes
"""

def test_add_track_with_mocks():
    library = MusicLibrary()
    mock_track_one = Mock()
    mock_track_one.matches.return_value = True
    mock_track_two = Mock()
    mock_track_two.matches.return_value = False
    library.add(mock_track_one)
    library.add(mock_track_two)
    assert library.search('Kano') == [mock_track_one]