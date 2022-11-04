"""
U PY svi testovi se pisu u fajlu koji pocinje sa 'test_' i pisu se kao funkcije ciji naziv pocinje sa 'test_'
Kada se napisu testovi, pokrecu se u terminalu komandom 'python3 -m pytest'
"""
import pytest
#markers - mark specific test cases to be executed

@pytest.mark.math
def test_one_plus_one():
    assert 1+1 == 2

#faled test
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c

#test with exception
def test_divide_by_zero():
    a = 1
    b = 0
    assert a / b == 0