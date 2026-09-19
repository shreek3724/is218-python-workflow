from app import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_add_negatives():
    assert add(-5, -2) == -7

def test_subtract_positive_result():
    """Test standard subtraction where the result is a positive integer."""
    assert subtract(10, 4) == 6

def test_subtract_negative_result():
    """
    Test distinct case: Subtracting a larger integer from a smaller integer
    to ensure the function correctly calculates and returns a negative value.
    """
    assert subtract(5, 12) == -7


# This file verifies that the add function returns the correct results for normal and negative inputs.