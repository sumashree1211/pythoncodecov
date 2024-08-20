import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math_functions import add, subtract, division

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(-10, -2) == 5
    assert division(10, -2) == -5
    try:
        division(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

if __name__ == "__main__":
   test_add()
   test_subtract()
   test_division()
   print("All tests passed.")