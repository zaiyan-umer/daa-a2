def _karatsuba_positive(x, y):
    if x < 10 or y < 10:
        return x * y

    m = max(len(str(x)), len(str(y))) // 2

    a = x // (10 ** m)
    b = x % (10 ** m)

    c = y // (10 ** m)
    d = y % (10 ** m)

    z0 = _karatsuba_positive(b, d)
    z2 = _karatsuba_positive(a, c)
    z1 = _karatsuba_positive(a + b, c + d) - z2 - z0

    return z2 * (10 ** (2 * m)) + z1 * (10 ** m) + z0


def karatsuba(x, y):
    if x == 0 or y == 0:
        return 0

    sign = -1 if (x < 0) ^ (y < 0) else 1

    result = _karatsuba_positive(abs(x), abs(y))

    return sign * result