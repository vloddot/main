from numb3rs import validate


def test_correct():
    assert validate('255.255.255.255')
    assert validate('192.168.1.4')
    assert validate('255.158.254.1')
    assert validate('213.48.13.2')


def test_false():
    assert not validate('275.3.6.28')
    assert not validate('301.238.475.2')
    assert not validate('cat.dog.1.4')
    assert not validate('64.128.256.512')
    assert not validate('256.255.255.255')
    assert not validate('123')
