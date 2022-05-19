from bank import value


def test_greetings_that_start_with_hello():
    assert value('HELLO, WORLD!') == 0
    assert value('hello, world!') == 0
    assert value('hello, David') == 0
    assert value('HELLo, DaViD') == 0
    assert value('hello, man') == 0


def test_greetings_that_start_with_h():
    assert value('hey, bro') == 20
    assert value('Hey, bro') == 20
    assert value('hey, man') == 20
    assert value('HEY, man') == 20
    assert value('hey, David') == 20
    assert value('how you doin\'?') == 20


def test_false_greetings():
    assert value('what up?') == 100
    assert value('WhaT uP') == 100
    assert value('what\'s up?') == 100
    assert value('') == 100
