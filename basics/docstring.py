def add_numbers(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (int, float): The first number to add.
    b (int, float): The second number to add.

    Returns:
    int, float: The sum of the two numbers.
    """
    return a + b

# Accessing the docstring using the __doc__ attribute
print(add_numbers.__doc__)

# Accessing the docstring using the help() function
help(add_numbers)



