"""
Karatsuba Integer Multiplication - Divide and Conquer algorithm.

Multiplies two large integers using the Karatsuba algorithm with
only three recursive multiplications per step.
"""


def _karatsuba_positive(x, y):
    """
    Multiply two non-negative integers using Karatsuba algorithm.

    Args:
        x: non-negative integer
        y: non-negative integer

    Returns:
        Product of x and y
    """
    # Base case: use built-in multiplication for small numbers
    if x < 10 or y < 10:
        return x * y

    # Determine split point: half the number of digits in the larger number
    m = max(len(str(x)), len(str(y))) // 2

    # Split x into a (high) and b (low)
    a = x // (10 ** m)
    b = x % (10 ** m)

    # Split y into c (high) and d (low)
    c = y // (10 ** m)
    d = y % (10 ** m)

    # Three recursive multiplications
    z0 = _karatsuba_positive(b, d)
    z2 = _karatsuba_positive(a, c)
    z1 = _karatsuba_positive(a + b, c + d) - z2 - z0

    # Combine: z2 * 10^(2m) + z1 * 10^m + z0
    return z2 * (10 ** (2 * m)) + z1 * (10 ** m) + z0


def karatsuba(x, y):
    """
    Multiplies two integers using Karatsuba multiplication.

    Handles positive and negative integers, zero, and different digit lengths.

    Args:
        x: integer
        y: integer

    Returns:
        Product of x and y
    """
    # Handle zero
    if x == 0 or y == 0:
        return 0

    # Determine sign
    sign = -1 if (x < 0) ^ (y < 0) else 1

    # Work with absolute values
    result = _karatsuba_positive(abs(x), abs(y))

    return sign * result