import numpy as np


def simpson_3_8(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("Number of subintervals must be a multiple of 3 for Simpson's 3/8 Rule.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    sum_multiples_of_3 = np.sum(y[3:-1:3])
    sum_remaining = np.sum(y[1:-1]) - sum_multiples_of_3

    result = (3 * h / 8) * (y[0] + 3 * sum_remaining + 2 * sum_multiples_of_3 + y[-1])

    print("""Formula:
    ∫ydx = 3h/8 (y0 + 2(y3+y6+...+yn-3) + 3(y1+y2+y4+y5+...+yn-2+yn-1) + yn)""")
    print(f"∫ydx = 3x{h}/8 ({y[0]} + 2({sum_multiples_of_3}) + 3({sum_remaining}) + {y[-1]})")
    print(f"∫ydx = {result}")
    print(f"Solution by Simpson's 3/8 Rule is {result}")

    return result


def simpson_3_8_discrete(x, y):
    if len(x) != len(y):
        raise ValueError("Length of x and y must be equal.")
    if len(x) % 3 != 1:
        raise ValueError("Number of points must be of the form 3n + 1 for Simpson's 3/8 Rule.")

    n = len(x) - 1
    h = (x[-1] - x[0]) / n

    sum_multiples_of_3 = np.sum(y[3:-1:3])
    sum_remaining = np.sum(y[1:-1]) - sum_multiples_of_3

    result = (3 * h / 8) * (y[0] + 3 * sum_remaining + 2 * sum_multiples_of_3 + y[-1])

    print("""Formula:
    ∫ydx = 3h/8 (y0 + 2(y3+y6+...+yn-3) + 3(y1+y2+y4+y5+...+yn-2+yn-1) + yn)""")
    print(f"∫ydx = 3x{h}/8 ({y[0]} + 2({sum_multiples_of_3}) + 3({sum_remaining}) + {y[-1]})")
    print(f"∫ydx = {result}")
    print(f"Solution by Simpson's 3/8 Rule is {result}")

    return result


# Keep the original function name for backwards compatibility
def simpsom_3_8(x, Fx, h):
    return simpson_3_8_discrete(x, Fx)