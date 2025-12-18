import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import add, subtract, multiply, divide


class TestCalculator:
    """Test cases for calculator functions."""

    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 5) == 10

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5

    def test_add_zero(self):
        """Test addition with zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(0, 0) == 0

    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 5) == 5

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-10, 5) == -15

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5

    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(4, 5) == 20

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(-4, -5) == 20

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0

    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        assert divide(6, 2) == 3
        assert divide(10, 5) == 2

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-6, 2) == -3
        assert divide(-10, -5) == 2

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_zero_by_number(self):
        """Test division of zero by a number."""
        assert divide(0, 5) == 0
        assert divide(0, -5) == 0


# Additional edge case tests
class TestCalculatorEdgeCases:
    """Test edge cases for calculator functions."""

    def test_large_numbers(self):
        """Test with large numbers."""
        large_num = 10**10
        assert add(large_num, large_num) == 2 * large_num
        assert subtract(large_num, large_num) == 0
        assert multiply(large_num, 2) == 2 * large_num
        assert divide(large_num, large_num) == 1

    def test_float_numbers(self):
        """Test with floating point numbers."""
        assert add(1.5, 2.5) == 4.0
        assert subtract(5.7, 2.2) == pytest.approx(3.5, rel=1e-9)
        assert multiply(2.5, 4.0) == 10.0
        assert divide(7.5, 2.5) == 3.0

    def test_very_small_numbers(self):
        """Test with very small numbers."""
        small_num = 1e-10
        assert add(small_num, small_num) == pytest.approx(2e-10)
        assert subtract(small_num, small_num) == pytest.approx(0, abs=1e-15)