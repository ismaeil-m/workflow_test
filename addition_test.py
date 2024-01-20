import numpy as np
from main import addition


def test_addition():
    val1 = 4
    val2 = 6
    assert addition(val1, val2) == 10


if __name__ == "__main__":
    test_addition()
    pass