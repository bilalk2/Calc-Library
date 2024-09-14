def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b
   
def divide(a, b):
    try:
        """Return the division of two numbers. """
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result
    