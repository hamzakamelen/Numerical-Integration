import numpy as np



def simpson_1_3(x, Fx):
    if len(x) != len(Fx):
        raise ValueError("Length of x and Fx must be equal.")
    if len(x) % 2 == 0:
        raise ValueError("Number of points must be odd (number of intervals must be even)")

    h = x[1] - x[0]
    n = len(x) - 1  # number of intervals

    sum_odd = sum(Fx[1:-1:2])
    sum_even = sum(Fx[2:-1:2])

    result = (h / 3) * (Fx[0] + 4 * sum_odd + 2 * sum_even + Fx[-1])
    return result


def simpson_1_3_func(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of subintervals must be even")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    Fx = f(x)


    return simpson_1_3(x, Fx)