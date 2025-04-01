[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gQ_doPhb)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15270862&assignment_repo_type=AssignmentRepo)
# APAi 5 Session 3 Assignment

Your description here.

# `int`
    Integer is a class in python. Which can create integer objects.
    int class can create objects using constructor method like below
        `a = int(1, base=10)`
    We can also create other base integers by passing `base` such as 2 for binary and 16 for hex etc.

    Also, if number is stored as string, i.e., a = '1' for example, then we can use int() to typecast the number from string to integer. 

# `encoded_from_base10`
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - the digit_map must not have any repeated character, else raises ValueError
    - Any in-built functions in the MATH module are used

# `digit_map`
    This variable holds the map of digits which will be used for encoding the number into some other base.

# `ValueError`
    This error is Raised when a function receives an argument of the right type but inappropriate value.

# `math`
    A mathematical tool box or module given by Python which supports mathematical operations

# `isclose`
    The math.isclose() function in Python determines whether two floating-point numbers are close to each other, using a relative tolerance or an absolute tolerance.
    Lets think of the scenario where this is useful. In first example lets say we have, 
    a = 0.001
    b = 0.002
    In second example lets say we have
    c = 1000.001
    d = 1000.002

    Now, although difference between a and b is same as c and d. when we see in reality, b is 50% higher than a. But d is 0.0001% heigher than c. In such cases relative tolerance comes in handy and math.isclose() implements the same function.

# `absolute`
    Absolute Tolerance (abs_tol): This specifies how close two numbers should be, in absolute terms. It is useful when comparing numbers that are very close to zero. The default value is 
0.0

# `relative`
    Relative Tolerance (rel_tol): This specifies how close two numbers should be, relative to the larger of the two numbers. It is a proportion of the larger value. The default value is 1e-9

# `tolerance`
    Tolance is the % deviation of accepted value from the expected (or Nominal) value

# `bin(`
    This returns the binary representation of the integer which is given as input

# `hex(`
    This returns the hexadecimal representation of the integer which is given as input

# `round`
# `truncation`
    The concepts of "rounding" and "truncation" are both methods used to reduce the number of digits in a number, but they follow different rules:

    Rounding
    Rounding involves adjusting a number to make it simpler, often to a specified number of decimal places or significant figures. The most common method of rounding is to look at the digit immediately after the place to which you are rounding and decide whether to round up or down based on that digit.

    Common Rounding Rules:
    Round Half Up (Standard Rounding): If the digit after the rounding place is 5 or greater, the last kept digit is increased by one. Otherwise, it remains the same.

    Example: Rounding 3.456 to two decimal places results in 3.46.
    Round Half Down: If the digit after the rounding place is 5 or greater, the last kept digit remains the same. Otherwise, it decreases by one.

    Example: Rounding 3.456 to two decimal places results in 3.45.
    Round Half to Even (Banker's Rounding): If the digit after the rounding place is exactly 5, the last kept digit is rounded to the nearest even number. This helps to reduce cumulative rounding errors.

    Example: Rounding 3.455 to two decimal places results in 3.46, and rounding 3.465 to two decimal places results in 3.46.
    Truncation
    Truncation involves cutting off digits after a certain point without rounding. This means that the number is simply shortened by removing all digits beyond a certain place, regardless of their value.

    Truncation Rule:
    The digits after the specified place are discarded without any consideration of their value. Truncation doesn't take the value away from the zero.
    Example: Truncating 3.456 to two decimal places results in 3.45.

# `equality`
    Equality is checks if two variable contents are same or dfferent

