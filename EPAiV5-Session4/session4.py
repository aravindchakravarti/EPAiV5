import random
import math
from decimal import *

class Qualean:
    '''
    This is a Qualean class. It takes (or generates) a number from [-1,0,1], multiplies with a 
    uniform distribution samples extracted between -1 to 1. Finally it rounds of the number to 
    10th of the decimal place
    It also has functions for mathematical operation on top of Qualean numbers
    '''
    def __init__(self, *args):
        '''
        Class iniatization. If parameter is given, then we take it. Else, we initializae with 
        randomly generated number with one of -1, 0, 1
        '''
        if args:
            if (args[0]<= 1 and args[0]>=-1):
                # Multiply the number with uniform random number and round it off
                self.number = round(args[0]*random.uniform(-1,1), 10)
                # self.number = round(Decimal(args[0]*random.uniform(-1,1), 10))
            else:
                raise ValueError ("Please provide the input with the digits between [-1,0,1] only")
        else:
            # Multiply the number with uniform random number and round it off
            self.number = round(random.randint(-1,1)*random.uniform(-1,1), 10)
            # self.number = round(Decimal(random.randint(-1,1)*random.uniform(-1,1), 10))

    def __repr__(self):
        '''
        Defines the representation of the Qualean class
        '''
        return 'Qualean Class Instance'

    def __and__(self, param = None):
        '''
        Implements the logical AND for the Qualean number. It works for both Qualean object and 
        also for int or float numbers
        '''
        if(isinstance(param, Qualean)):
            return(bool(self.number) and bool(param.return_qualean()))
        elif (isinstance(param, int) or isinstance(param, float)):
            return(bool(self.number) and bool(param))
        elif (param == None):
            return(False)
        else:
            raise TypeError

    def __or__(self, param):
        '''
        Implements the logical OR for the Qualean number. It works for both Qualean object and 
        also for int or float numbers
        '''
        if(isinstance(param, Qualean)):
            return(bool(self.number) or bool(param.return_qualean()))
        elif (isinstance(param, int) or isinstance(param, float)):
            return(bool(self.number) or bool(param))
        elif (param == None):
            return(True)
        else:
            raise TypeError

    def __str__(self):
        '''
        String representation of Qualean class
        '''
        return(f'Qualean String for number: {self.number}')

    def __add__(self, param):
        '''
        Adds either two Qualean numbers or One Qualean number and one int/float number
        '''
        if (isinstance(param, Qualean)):
            return(self.number + param.return_qualean())
        elif (isinstance(param, int) or isinstance(param, float)):
            return(self.number + param)
        else:
            raise TypeError

    def __eq__(self, param):
        '''
        Checks if to Qualean numbers or One Qualean and another int/float numbers are equal
        '''
        if (isinstance(param, Qualean)):
            return(self.number == param.return_qualean())
        elif (isinstance(param, int) or isinstance(param, float)):
            return(self.number == param)
        else:
            raise TypeError

    def __float__(self):
        '''
        Returns the float value of the Qualean number
        '''
        return float(self.number)

    def __ge__(self, param):
        '''
        Checks if Qualean number is greater than or equal to given Qualean/int/float number
        '''
        if (isinstance(param, Qualean)):
            return(self.number >= param.return_qualean())
        elif (isinstance(param, int) or isinstance(param, float)):
            return(self.number >= param)
        else:
            raise TypeError

    def __gt__(self, param):
        '''
        Checks if Qualean number is greater than given Qualean/int/float number
        '''
        if (isinstance(param, Qualean)):
            return(self.number > param.return_qualean())
        elif (isinstance(param, int) or isinstance(param, float)):
            return(self.number > param)
        else:
            raise TypeError

    def __invertsign__(self):
        '''
        Inverts the sign of Qualean number
        '''
        return (-1*self.number)

    def __le__(self, param):
        '''
        Checks if Qualean number is less than or equal to the given Qualean/int/float number
        '''
        if (isinstance(param, Qualean)):
            return(self.number <= param.return_qualean())
        elif (isinstance(param, int) or isinstance(param, float)):
            return(self.number <= param)
        else:
            raise TypeError

    def __lt__(self, param):
        '''
        Checks if Qualean number is less than the given Qualean/int/float number
        '''
        if (isinstance(param, Qualean)):
            return(self.number < param.return_qualean())
        elif (isinstance(param, int) or isinstance(param, float)):
            return(self.number < param)
        else:
            raise TypeError

    def __mul__(self, param):
        '''
        Mulitplies the given number (Qualean/int/float) with Qualean number
        '''
        if (isinstance(param, Qualean)):
            return(self.number * param.return_qualean())
        elif (isinstance(param, int) or isinstance(param, float)):
            return(self.number * param)
        else:
            raise TypeError

    def __sqrt__(self):
        '''
        Returns the square root of Qualean number
        '''
        if self.number < 0:
            return (str(round(Decimal(math.sqrt(self.__invertsign__())), 10)) + 'i')
        else:
            return (round(Decimal(math.sqrt(self.number)),10))

    def __bool__(self):
        '''
        Returns the boolean value of the Qualean number. 
        If 0 then False
        If any other value (0.1, 1, 5, or -0.1, -0.5. -2.5) then True
        '''
        return(bool(self.number))

    def return_qualean(self):
        '''
        Returns the Qualean number
        '''
        return(self.number)