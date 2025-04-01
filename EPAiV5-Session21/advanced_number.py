class AdvancedNumber:
    """
    A class that encapsulates a numeric value and supports arithmetic, 
    comparison operations, and other Python special methods.
    """
    
    def __init__(self, number=0):
        """
        Initialize the AdvancedNumber with a given value.

        Args:
            number (int, float): The initial value of the object. Defaults to 0.
        """
        self.value = number

    def __del__(self):
        """
        Destructor called when the object is about to be destroyed.
        Prints a message indicating the value being destroyed.
        """
        print(f"AdvancedNumber with value {self.value} is being destroyed")

    def __str__(self):
        """
        Returns a user-friendly string representation of the object.

        Returns:
            str: A formatted string showing the value of the object.
        """
        return f"Value: {self.value}"
    
    def __repr__(self):
        """
        Returns a detailed string representation for debugging.

        Returns:
            str: A string in the format 'AdvancedNumber(value)'.
        """
        return f"AdvancedNumber({self.value})"
    
    def __add__(self, other):
        """
        Adds two AdvancedNumber objects.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            AdvancedNumber: A new object with the sum of the two values.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if not isinstance(other, AdvancedNumber):
            raise ValueError("Operand must be of type AdvancedNumber")
        return AdvancedNumber(self.value + other.value)
    
    def __sub__(self, other):
        """
        Subtracts another AdvancedNumber object from the current one.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            AdvancedNumber: A new object with the difference of the two values.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if not isinstance(other, AdvancedNumber):
            raise ValueError("Operand must be of type AdvancedNumber")
        return AdvancedNumber(self.value - other.value)
    
    def __mul__(self, other):
        """
        Multiplies the current object with another number.

        Args:
            other (AdvancedNumber, int, float): The object or number to multiply.

        Returns:
            AdvancedNumber: A new object with the product of the multiplication.

        Raises:
            ValueError: If the operand is not AdvancedNumber, int, or float.
        """
        if isinstance(other, (AdvancedNumber, int, float)):
            return AdvancedNumber(self.value * (other.value if isinstance(other, AdvancedNumber) else other))
        raise ValueError("Operand must be AdvancedNumber, int, or float")
    
    def __truediv__(self, other):
        """
        Divides the current object by another number.

        Args:
            other (AdvancedNumber, int, float): The object or number to divide by.

        Returns:
            AdvancedNumber: A new object with the quotient.

        Raises:
            ValueError: If the operand is not AdvancedNumber, int, or float.
            ValueError: If attempting to divide by zero.
        """
        if isinstance(other, (AdvancedNumber, int, float)):
            divisor = other.value if isinstance(other, AdvancedNumber) else other
            if divisor == 0:
                raise ValueError("Cannot divide by zero")
            return AdvancedNumber(self.value / divisor)
        raise ValueError("Operand must be AdvancedNumber, int, or float")
    
    def __mod__(self, other):
        """
        Computes the modulus with another AdvancedNumber.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            AdvancedNumber: A new object with the modulus result.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value % other.value)
        raise ValueError("Operand must be of type AdvancedNumber")
    
    def __gt__(self, other):
        """
        Checks if the current value is greater than another.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            bool: True if greater, False otherwise.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if isinstance(other, AdvancedNumber):
            return self.value > other.value
        raise ValueError("Operand must be of type AdvancedNumber")
    
    def __ne__(self, other):
        """
        Checks if the current value is not equal to another.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            bool: True if not equal, False otherwise.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if isinstance(other, AdvancedNumber):
            return self.value != other.value
        raise ValueError("Operand must be of type AdvancedNumber")
    
    def __ge__(self, other):
        """
        Checks if the current value is greater than or equal to another.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            bool: True if greater or equal, False otherwise.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if isinstance(other, AdvancedNumber):
            return self.value >= other.value
        raise ValueError("Operand must be of type AdvancedNumber")
    
    def __hash__(self):
        """
        Returns the hash value of the object.

        Returns:
            int: The hash of the value.
        """
        return hash(self.value)
    
    def __call__(self):
        """
        Makes the object callable, returning the square of its value.

        Returns:
            int, float: The square of the current value.
        """
        return self.value ** 2
    
    def __bool__(self):
        """
        Returns the boolean value of the object.

        Returns:
            bool: True if the value is non-zero, False otherwise.
        """
        return bool(self.value)
    
    def __format__(self, format_spec):
        """
        Formats the value according to the given format specifier.

        Args:
            format_spec (str): The format specification.

        Returns:
            str: The formatted string.
        """
        return format(self.value, format_spec)
