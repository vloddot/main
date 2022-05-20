from plates import is_valid


def test_valid():
    assert is_valid('CS50')
    assert is_valid('HELLO')
    assert is_valid('CSCOOL')
    assert is_valid('ECTO88')


def test_less_than_two_letters_start():
    assert not is_valid('M0RE')
    assert not is_valid('0OHI')
    assert not is_valid('50SC')
    assert not is_valid('12ABCD')
    assert not is_valid('3XmEw')


def test_less_than_two_letters():
    assert not is_valid('h')
    assert not is_valid('H')
    assert not is_valid('x')


def test_more_than_six_letters():
    assert not is_valid('OUTATIME')


def test_number_in_middle():
    assert not is_valid('AA22AA')
    assert not is_valid('AAA22A')


def test_zero_at_start():
    assert not is_valid('CS05')


def test_punctuation():
    assert not is_valid('PI3.14')
    assert not is_valid('.,URW')
