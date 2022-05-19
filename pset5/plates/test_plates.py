from plates import is_valid

def test_valid():
    assert is_valid('CS50')
    assert is_valid('HELLO')
    assert is_valid('CSCOOL')

def test_less_than_two_letters_start():
    assert not is_valid('M0RE')

def test_less_than_two_letters():
    assert not is_valid()

def test_more_than_two_letters():
    pass

def test_number_in_middle():
    pass

def test_zero_at_start():
    pass

def test_punctuation():
    pass
