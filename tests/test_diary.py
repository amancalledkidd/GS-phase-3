from lib.diary import Diary

"""
Create instance of diary 
read returns contents
"""

def test_diary_read():
    diary = Diary("Hello, World")
    assert diary.read() == 'Hello, World'