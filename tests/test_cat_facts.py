from lib.cat_facts import CatFacts
from unittest.mock import Mock


"""
make instance of class
test provide
returns cat fact
"""

def test_provide_fact_provide():
    mock_requester = Mock()
    mock_response = Mock()
    mock_requester.get.return_value = mock_response
    mock_response.json.return_value = {"fact": 'Cats have facts'}
    cat_facts = CatFacts(mock_requester)
    assert cat_facts.provide() == 'Cat fact: Cats have facts'