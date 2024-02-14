from function import make_capital, make_lower, make_upper

def test_upper():
    assert make_upper("hello") == "HELLO"
    assert make_upper("Python") == "PYTHON"
    assert make_upper("pHiTrOn") == "PHITRON"

def test_lower():
    assert make_lower("HELLO") == "hello"
    assert make_lower("Python") == "python"
    assert make_lower("pHiTrOn") == "phitron"

def test_capital():
    assert make_capital("hello") == "Hello"
    assert make_capital("Python") == "Python"
    assert make_capital("pHiTrOn") == "Phitron"