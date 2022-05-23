from twttr import shorten


def test_word_with_vowels():
    assert shorten('jUst sEttIng Up my twIttEr') == 'jst sttng p my twttr'
    assert shorten('HElLO, wOrld!') == 'HlL, wrld!'
    assert shorten('hello, world') == 'hll, wrld'
    assert shorten('stUpId mAn123') == 'stpd mn123'


def test_word_without_vowels():
    assert shorten('') == ''
    assert shorten('bvjkqwsfxz') == 'bvjkqwsfxz'
