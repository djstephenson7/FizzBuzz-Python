import pytest
import fizzbuzz

def test_calc_total():
    total = fizzbuzz.calc_total(4,5)
    assert total == 9

def test_calc_multiply():
    result = fizzbuzz.calc_multiply(10,3)
    assert result == 30
