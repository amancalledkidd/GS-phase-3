from lib.diary import Diary
from lib.secret_diary import SecretDiary
import pytest

"""
create Diary instance
create secret diary instance using diary
try to read contents
returns go away
"""

def test_secret_diary_read():
    diary = Diary('Welcome to my diary')
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as error:
        secret_diary.read()
    assert str(error.value) == 'Go away!'

"""
create diary instance
create secret diary
unlock contents
read contents
returns contents
"""

def test_secret_diary_unlock_and_read():
    diary = Diary('Welcome to my diary')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'Welcome to my diary'


"""
create diary instance
create secret diary
unlock contents
read contents
lock contents
read contents
check for exception
return Go away
"""

def test_secret_diary_unlock_lock_read():
    diary = Diary('Welcome to my diary')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'Welcome to my diary'
    secret_diary.lock()
    with pytest.raises(Exception) as error:
        secret_diary.read()
    assert str(error.value) == 'Go away!'