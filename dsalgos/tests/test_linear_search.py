from src.algos.search.linear_search import linear_search

def test_linear_search():
    a = [1, 2, 3]
    assert linear_search(a, 1) == True
    assert linear_search(a, 0) == False
