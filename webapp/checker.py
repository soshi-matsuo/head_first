from flask import session
from functools import wraps

def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are not logged in.'
    return wrapper

# check_logged_in(function)は
# @check_logged_in
# def function():~~と全く同じ意味