def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    if (base < 2 or base > 36):
        raise ValueError("The base should be within 2 to 32")

    if (len(set(digit_map)) != len(digit_map)):
        raise ValueError("There are  repeating  charecters in the digit_map")

    if (len(set(digit_map)) != base):
        raise ValueError("Length of digit_map must be equal to base ")

    neg = 1
    if number < 0:
        neg = -1

    number = abs(number)
    conv_string = ''
    while (number):
        whole_divider = number//base
        reminder = number-(base*whole_divider)
        conv_string = conv_string + str(digit_map[reminder])
        number = whole_divider

    if (neg == -1):
        conv_string = conv_string + '-'

    reversed_string = conv_string[::-1]

    return reversed_string


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    abs_tol = 1e-05
    rel_tol = 1e-12
    '''
    return (abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol))
    '''
    abs_error = abs(a-b)
    relative_error = rel_tol*max(abs(a), abs(b))
    if (abs_tol < relative_error) or (abs_error < abs_tol):
        return True
    else:
        return False

def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    if (type(f_num) == int or type(f_num) == float):
        return(int (f_num))

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    neg = 1
    if (type(f_num) == int or type(f_num) == float):
        if (f_num < 0):
            neg = -1

        whole_number = manual_truncation_function(abs(f_num))
        residue = abs(f_num) - whole_number
        if residue >= 0.5:
            whole_number = whole_number + 1

    return (neg * whole_number)

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    from fractions import Fraction
    neg = 1
    if (type(f_num) == int or type(f_num) == float):
        if (f_num < 0):
            neg = -1

        fraction_num = Fraction(abs(f_num)).limit_denominator(1e12)
        integer_part_of_num = fraction_num.numerator
        residue = abs(f_num) - integer_part_of_num
        if residue >= 0.5:
            integer_part_of_num = integer_part_of_num + 1

    return (neg*integer_part_of_num)
