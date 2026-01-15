#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Compute the factorial of a non-negative integer using recursion.
        The factorial of n (written n!) is the product of all integers from n down to 1.
        By definition, 0! = 1.

    Parameters:
        n (int): A non-negative integer whose factorial will be computed.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
