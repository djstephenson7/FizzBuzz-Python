import pytest
import fizzbuzzpython

def fizzbuzz_num(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def fizzbuzz(i):
    for num in range(1,101):
        print(num)

def test_three():
    assert fizzbuzz_num(3) == "Fizz"

def test_seven():
    assert fizzbuzz_num(7) == 7

def test_buzz():
    assert fizzbuzz_num(5) == "Buzz"

def test_fizzbuzz():
    assert fizzbuzz_num(15) == "FizzBuzz"
