from lib.secret_diary import SecretDiary
from unittest.mock import Mock
import pytest

"""
create mock diary instance
create secret diary instance
read diary returns go away
"""

def test_secret_diary_locked_read():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as error:
        secret_diary.read()
    assert str(error.value) == 'Go away!'
    diary.read.assert_not_called()

"""
create mock diary instance
crete mock contents in diary 
create secret diary instance
unlock diary
read diary 
returns contents
"""

def test_secret_diary_unlock_read():
    diary = Mock()
    diary.read.return_value = 'Hello'
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'Hello'


"""
create mock diary instance
crete mock contents in diary 
create secret diary instance
unlock diary
read diary 
lock diary
read diary
return go away
"""
def test_secret_diary_unlock_lock_read():
    diary = Mock()
    diary.read.return_value = 'Hello'
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'Hello'
    secret_diary.lock()
    with pytest.raises(Exception) as error:
        secret_diary.read()
    assert str(error.value) == 'Go away!'
    diary.read.assert_not_called()