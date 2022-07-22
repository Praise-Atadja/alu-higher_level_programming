#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = safe_print_division(a, b)
    except (ZeroDivisionError, ValueError, RuntimeError, TypeError):
        quotient = None
    finally:
        print("Inside result:{:d} / {:d} = {}".format(a, b, quotient))
        return(quotient)
