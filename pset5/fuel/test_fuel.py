from fuel import convert, gauge


def test_convert():
    assert convert('3/4') == 75
    assert convert('0/4') == 0
    assert convert('1/2') == 50
    assert convert('4/5') == 80


def test_gauge():
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(67) == '67%'
    assert gauge(20) == '20%'
    assert gauge(0.5) == 'E'
