### Tests for function within the app.py file
from nlp_lib.app import summarise_wiki, search_wiki


def test_summarise_wiki():
    assert "Python" in summarise_wiki("Python (programming language)")


def test_search_wiki():
    assert "Python" in search_wiki("Python")
