from lib.music_library import MusicLibrary
from lib.track import Track
import pytest

""" 
test add by adding two tracks
return track list
"""

def test_add_track():
    library = MusicLibrary()
    track_one = Track('Hello' , 'Kano')
    track_two = Track('Hero', 'J.cole')
    library.add(track_one)
    library.add(track_two)
    assert library.tracks == [track_one, track_two]


""" 
test add by adding two tracks
search for one track
return track in list
"""
# @pytest.mark.skip
def test_track_search():
    library = MusicLibrary()
    track_one = Track('Hello' , 'Kano')
    track_two = Track('Hero', 'J.cole')
    library.add(track_one)
    library.add(track_two)
    assert library.search('Kano') == [track_one]

"""
Add three tracks 
search for for partial name
returns list with two tracks
"""


def test_track_search_case_sensitive():
    library = MusicLibrary()
    track_one = Track('Hello' , 'Kano')
    track_two = Track('Hero', 'J.cole')
    track_three = Track('Hueamann', 'A man called hero')
    library.add(track_one)
    library.add(track_two)
    library.add(track_three)
    assert library.search('hero') == [track_two, track_three]
