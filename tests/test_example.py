from hexlet_pytest.example import reverse

def test_reverse():
    assert reverse('Abc') == 'cbA'
    

def test_reverse_for_empty_string():
    assert reverse('') == ''
