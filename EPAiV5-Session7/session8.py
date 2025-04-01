from functools import wraps, singledispatch
from datetime import datetime
from time import perf_counter
from typing import Callable

def odd_it(fn: Callable)->Callable:
    '''
    This is a decorator function which decorates any function such that, decorated function
    gets executed only in odd second.
    '''
    if not callable(fn):
        raise TypeError('Called with non-function argument')

    @wraps(fn)
    def inner(*args, **kwargs):
        '''
        Returns None if current second is a even second
        Executes the functions and returns the value if odd second 
        '''

        # Check if odd second
        if(datetime.now().second % 2):
            return(fn(*args, **kwargs))
        else:
            return None

    return inner

def logger(fn: Callable)-> Callable:
    '''
    This is a decorator which helps in logging the data if decorated to a function
    This decorator logs below items
    1. Function Name
    2. Execution Time
    3. Function Description
    4. Function annotation
    5. Called parameters and type
    '''
    if not callable(fn):
        raise TypeError('Called with non-function argument')

    @wraps(fn)
    def inner(*args, **kwargs):
        '''
        This is the inner function which executes passed function along with 
        ammending/logging some details
        '''
        # Get the start of execution time
        start_time = perf_counter()

        # Get the function name and execute the function
        print(f'function_name is {fn.__name__} and called at {start_time}')
        return_values = fn(*args, **kwargs)

        # Get the function end time and hence execution time
        print(f'Execution time is {perf_counter() - start_time}')

        # Get the function description, and annoations
        print(f'Function description {fn.__doc__}')
        print(f'Function annotation {fn.__annotations__}')

        # Log the called parameters and their types
        print('Called parameters and their types:')
        for arg, value in zip(fn.__code__.co_varnames, args):
            print(f'{arg}: {value} ({type(value).__name__})')
        for key, value in kwargs.items():
            print(f'{key}: {value} ({type(value).__name__})')

        return return_values

    return inner


def decorator_factory(access:str):
    '''
    This is a decorator factory, which takes below mentioned string and provides access to 
    variables as mentioned below
    'high' : Access to 4 variables
    'mid'  : Access to 3 variables
    'low'  : Access to 2 variables
    'no'   : Access to 1 variable 
    '''
    var_1 = 0
    var_2 = 0
    var_3 = 0
    var_4 = 0
    def inner_decorator(fn: Callable) -> Callable:
        '''
        Checks the access passed by the decorator factory and returns the 
        corresponding decorator
        '''
        if access == 'high':
            @wraps(fn)
            def wrapper(*args, **kwargs):
                return fn(var_1, var_2, var_3, var_4)
        elif access == 'mid':
            @wraps(fn)
            def wrapper(*args, **kwargs):
                return fn(var_1, var_2, var_3)
        elif access == 'low':
            @wraps(fn)
            def wrapper(*args, **kwargs):
                return fn(var_1, var_2)
        elif access == 'no':
            @wraps(fn)
            def wrapper(*args, **kwargs):
                return fn(var_1)
        else:
            @wraps(fn)
            def wrapper(*args, **kwargs):
                return "Improper access keyword set"

        return wrapper

    return inner_decorator


def authenticate(set_password: str) -> Callable:
    '''
    This function is a decorator factory, which stores the password and will be compared 
    against the password when used with the decorator.
    '''
    def password_verify(fn: Callable) -> Callable:
        '''
        This function decorates the function, and it is expected that, first argument of the
        function is a password
        '''
        def inner(*args, **kwargs):
            '''
            This function executes the function in following cases
            if no args provided : Raise TypeError, as there are no-arguments/passord
            if 1st arg maches with set_passord : Executes the function
            else : Returns saying wrong passord
            '''
            if not args:
                raise TypeError("Password not provided")
            if args[0] == set_password:
                return fn(*args, **kwargs)  # Ensure the function result is returned
            else:
                return "Wrong Password"
        return inner
    return password_verify


def timed(reps:int) -> Callable:
    '''
    This is a decorator factory, which repeatedly calls the decoratd function for 'reps' time
    and captures the average time it took to execute the decorated function
    '''
    def decorate_function(fn: Callable) -> Callable:
        '''
        Decorates the function 'fn' (adds features on top of fn)
        '''
        @wraps(fn)
        def inner(*args, **kwargs):
            '''
            Captures the time it took to execute the function
            '''
            time_taken = []
            for index in range(reps):
                start = perf_counter()
                return_value = fn(*args, **kwargs)
                end = perf_counter()
                time_taken.append(end-start)

            print(f'Average time taken to run fn.__name__ is {sum(time_taken)/reps} and repeated for {reps} times')

            return return_value

        return inner

    return decorate_function