from lib.task_list import TaskList
from unittest.mock import Mock

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

"""
add two tasks
use all to call list
"""

def test_add_tasks():
    task_list = TaskList()
    mock_task_one = Mock()
    mock_task_two = Mock()
    task_list.add(mock_task_one)
    task_list.add(mock_task_two)
    assert task_list.all() == [mock_task_one, mock_task_two]

"""
add three task
two classes are complete
returns list of complete tasks
"""

def test_add_tasks():
    task_list = TaskList()
    mock_task_one = FakeIsComplete()
    mock_task_two = FakeIsComplete()
    task_list.add(mock_task_one)
    task_list.add(mock_task_two)
    assert task_list.all_complete() == True

class FakeIsComplete():
    def is_complete(self):
        return True
    


"""
add three task
one classes are complete
returns false
"""

def test_add_tasks():
    task_list = TaskList()
    mock_task_one = FakeIsComplete()
    mock_task_two = FakeIsComplete()
    mock_task_three = FakeIsNotComplete()
    task_list.add(mock_task_one)
    task_list.add(mock_task_two)
    task_list.add(mock_task_three)
    assert task_list.all_complete() == False

class FakeIsNotComplete():
    def is_complete(self):
        return False
    