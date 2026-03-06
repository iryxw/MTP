from src.lab81 import is_even


def test_is_even_positive():
  assert is_even(4) is True
  assert is_even(10) is True


def test_is_even_negative():
  assert is_even(3) is False
  assert is_even(7) is False


def test_is_even_zero():
  assert is_even(0) is True