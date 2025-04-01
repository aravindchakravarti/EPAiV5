[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/aSZOkvTK)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15304031&assignment_repo_type=AssignmentRepo)
# epai5session4 Assignment

Code defines a custom class named Qualean that demonstrates various Python magic methods, also known as dunder (double underscore) methods. These methods allow instances of the Qualean class to interact with standard Python operations and functions in a customized manner. Below is a detailed explanation of the class and its methods, incorporating the specified terms:

# Initialization (init)
The __init__ method is a constructor that initializes a new instance of the Qualean class. It can take an optional argument. If an argument is provided, it checks whether the argument is between -1 and 1 (inclusive). If it is, it multiplies this value by a random number between -1 and 1 and rounds it to 10 decimal places to set self.number. If the argument is not in the range, it raises a ValueError. If no argument is provided, it randomly selects -1, 0, or 1, multiplies this value by a random number between -1 and 1, and rounds it to 10 decimal places to set self.number.

# Representation (repr)
The __repr__ method defines the string representation of an instance of the class. It returns the string 'Qualean Class Instance', which can be useful for debugging.

# Logical AND (and)
The __and__ method implements the logical AND operation. It checks if the parameter is an instance of the Qualean class, an integer, or a float. If it is a Qualean, it performs a logical AND operation between the boolean values of self.number and param.return_qualean(). If it's an integer or float, it performs a logical AND operation between the boolean values of self.number and the parameter. If no parameter is provided, it returns False.

# Logical OR (or)
The __or__ method implements the logical OR operation. Similar to the __and__ method, it checks the type of the parameter and performs a logical OR operation accordingly. If no parameter is provided, it returns True.

# String Representation (str)
The __str__ method defines the string representation of an instance when str() is called. It returns a formatted string including the value of self.number.

# Addition (add)
The __add__ method defines the addition operation. It checks the type of the parameter and returns the sum of self.number and the parameter. If the parameter is a Qualean, it adds self.number to param.return_qualean(). If the parameter is an integer or float, it adds self.number to the parameter.

# Equality (eq)
The __eq__ method defines the equality comparison operation. It checks the type of the parameter and compares self.number to the parameter. If the parameter is a Qualean, it compares self.number to param.return_qualean(). If the parameter is an integer or float, it compares self.number to the parameter.

# Float Conversion (float)
The __float__ method allows conversion of a Qualean instance to a float. It returns self.number as a float.

# Greater Than or Equal To (ge)
The __ge__ method defines the greater than or equal to comparison operation. It checks the type of the parameter and compares self.number to the parameter. If the parameter is a Qualean, it compares self.number to param.return_qualean(). If the parameter is an integer or float, it compares self.number to the parameter.

# Greater Than (gt)
The __gt__ method defines the greater than comparison operation. It checks the type of the parameter and compares self.number to the parameter. If the parameter is a Qualean, it compares self.number to param.return_qualean(). If the parameter is an integer or float, it compares self.number to the parameter.

# Invert Sign (invertsign)
The __invertsign__ method returns the negation of self.number.

# Less Than or Equal To (le)
The __le__ method defines the less than or equal to comparison operation. It checks the type of the parameter and compares self.number to the parameter. If the parameter is a Qualean, it compares self.number to param.return_qualean(). If the parameter is an integer or float, it compares self.number to the parameter.

# Multiplication (mul)
The __mul__ method defines the multiplication operation. It checks the type of the parameter and returns the product of self.number and the parameter. If the parameter is a Qualean, it multiplies self.number by param.return_qualean(). If the parameter is an integer or float, it multiplies self.number by the parameter.

# Square Root (sqrt)
The __sqrt__ method returns the square root of self.number. It uses the math.sqrt function to compute the square root.

# Boolean Conversion (bool)
The __bool__ method allows a Qualean instance to be evaluated in a boolean context. It returns the boolean value of self.number.

# Returning the Qualean Value (return_qualean)
The return_qualean method is a simple method that returns self.number