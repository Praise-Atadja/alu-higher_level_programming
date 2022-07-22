#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = safe_print_division(a, b)
    except (ZeroDivisionError, ValueError, RuntimeError, TypeError):
       return None
    finally:
        print("Inside result:{:d} / {:d} = {}".format(a, b, quotient))
    
