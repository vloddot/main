from jar import Jar
from pytest import raises


def test_init():
    Jar(12)
    with raises(ValueError) as exc:
        Jar(-1)
        Jar('Hello!')


def test_deposit():
    jar = Jar(12)
    jar.deposit(3)
    assert jar.size == 3 and jar.capacity == 12
    with raises(ValueError) as exc:
        jar.deposit(10)


def test_withdraw():
    jar = Jar(12)
    jar._cookie_num = 3
    jar.withdraw(2)
    with raises(ValueError) as exc:
        jar.withdraw(2)


def test_str():
    jar = Jar(12)
    assert str(jar) == ''
    jar._cookie_num = 3
    assert str(jar) == '🍪🍪🍪'
