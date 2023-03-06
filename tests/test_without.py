from hexlet_pytest.without import without

def test_without():
    assert without([], 5) == []
    assert without([1, 2, 4, 5, 4, 7, 4], 4, 2) == [1, 5, 7]