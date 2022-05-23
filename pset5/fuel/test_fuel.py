import pytest
from fuel import convert, gauge


def test_convert():
    with pytest.raises(ValueError) as exc:
        x = convert('2/1')

    with pytest.raises(ValueError) as exc:
        x = convert('0.5/2')

    with pytest.raises(ZeroDivisionError) as exc:
        x = convert('1/0')
        
    assert convert('3/4') == 75
    assert convert('2/4') == 50
    assert convert('0/6') == 0
    assert convert('1/7') == 14


def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(0) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'