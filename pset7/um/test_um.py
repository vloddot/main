from um import count


def test_one_um():
    assert count('um') == 1
    assert count(' um ') == 1
    assert count(' um, ') == 1


def test_one_um_with_additional_words():
    assert count('Hello, um, world.') == 1
    assert count('This is, um... CS50.') == 1
    assert count('Um... what are regular expressions? ') == 1


def test_two_ums():
    assert count('um, um') == 2
    assert count(' um, um,') == 2


def test_two_ums_with_additional_words():
    assert count('Um, thanks, um, regular expressions make sense now.') == 2


def test_two_ums_with_additional_overlapping_with_um_words():
    assert count('Um? Mum? Is this that album where, um, the clumsy alums play drums?') == 2
