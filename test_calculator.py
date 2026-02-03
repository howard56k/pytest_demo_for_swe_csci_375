"""
Unit tests for calculator module.
"""
import pytest
from calculator import add, subtract, multiply, divide, power


class TestAdd:
    """Test cases for add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.7) == pytest.approx(6.2)


class TestSubtract:
    """Test cases for subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-2, -3) == 1
    
    def test_subtract_mixed_numbers(self):
        """Test subtracting with mixed signs."""
        assert subtract(5, -3) == 8
    
    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5


class TestMultiply:
    """Test cases for multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(3, 4) == 12
    
    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        assert multiply(-2, -3) == 6
    
    def test_multiply_mixed_numbers(self):
        """Test multiplying with mixed signs."""
        assert multiply(-2, 3) == -6
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
    
    def test_multiply_by_one(self):
        """Test multiplying by one."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5


class TestDivide:
    """Test cases for divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(10, 2) == 5
    
    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        assert divide(-10, -2) == 5
    
    def test_divide_mixed_numbers(self):
        """Test dividing with mixed signs."""
        assert divide(-10, 2) == -5
    
    def test_divide_by_one(self):
        """Test dividing by one."""
        assert divide(5, 1) == 5
    
    def test_divide_floats(self):
        """Test dividing with floating point numbers."""
        assert divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestPower:
    """Test cases for power function."""
    
    def test_power_positive_base_positive_exponent(self):
        """Test raising positive base to positive exponent."""
        assert power(2, 3) == 8
    
    def test_power_positive_base_zero_exponent(self):
        """Test raising any number to zero."""
        assert power(5, 0) == 1
    
    def test_power_positive_base_negative_exponent(self):
        """Test raising positive base to negative exponent."""
        assert power(2, -2) == 0.25
    
    def test_power_zero_base(self):
        """Test raising zero to a power."""
        assert power(0, 5) == 0
    
    def test_power_one_exponent(self):
        """Test raising to power of one."""
        assert power(5, 1) == 5
