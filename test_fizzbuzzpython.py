import pytest
import fizzbuzzpython as fb

def test_three():
    assert fb.fizzbuzz(3) == "Fizz"

def test_seven():
    assert fb.fizzbuzz(7) == 7

def test_buzz():
    assert fb.fizzbuzz(5) == "Buzz"

def test_fizzbuzz():
    assert fb.fizzbuzz(15) == "FizzBuzz"
