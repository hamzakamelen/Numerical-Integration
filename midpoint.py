import numpy as np

def midpoint_rule(f, a, b, n):
    """
    Perform numerical integration using the Midpoint Rule.

    The Midpoint Rule approximates the definite integral of a function f(x)
    over the interval [a, b] by dividing the interval into n subintervals
    and summing the function values at the midpoint of each subinterval.

    Formula:
    ∫[a to b] f(x) dx ≈ h * Σ[i=1 to n] f(x_i)

    where:
    h = (b - a) / n
    x_i = a + (i - 1/2) * h

    Parameters:
    f (function): The function to integrate
    a (float): Lower bound of integration
    b (float): Upper bound of integration
    n (int): Number of subintervals

    Returns:
    float: Approximation of the definite integral
    """
    # Step 1: Calculate the width of each subinterval
    h = (b - a) / n
    print(f"Step 1: Calculate h = (b - a) / n = ({b} - {a}) / {n} = {h}")

    # Step 2: Generate midpoints of subintervals
    x = np.linspace(a + h / 2, b - h / 2, n)
    print(f"Step 2: Generate midpoints: {x}")

    # Step 3: Evaluate function at midpoints
    y = f(x)
    print(f"Step 3: Evaluate function at midpoints: {y}")

    # Step 4: Calculate the sum of function values
    sum_y = np.sum(y)
    print(f"Step 4: Calculate sum of function values: {sum_y}")

    # Step 5: Calculate the final result
    result = h * sum_y
    print(f"Step 5: Calculate final result: h * sum = {h} * {sum_y} = {result}")

    print("\nMidpoint Rule Formula:")
    print(f"∫[{a} to {b}] f(x) dx ≈ {h} * ({' + '.join([f'f({xi:.2f})' for xi in x])})")
    print(f"                    ≈ {h} * {sum_y}")
    print(f"                    ≈ {result}")

    return result

def midpoint_rule_discrete(x, y):
    """
    Perform numerical integration using the Midpoint Rule for discrete data points.

    The Midpoint Rule for discrete data approximates the area under the curve
    represented by the data points using rectangles centered at each point.

    Formula:
    ∫ y dx ≈ Σ[i=1 to n-1] (x[i+1] - x[i]) * y[i]

    Parameters:
    x (array-like): x-coordinates of data points
    y (array-like): y-coordinates of data points

    Returns:
    float: Approximation of the definite integral
    """
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")

    n = len(x)
    result = 0

    print("Midpoint Rule for Discrete Data:")
    print("Formula: ∫ y dx ≈ Σ (x[i+1] - x[i]) * y[i]")

    for i in range(n - 1):
        dx = x[i + 1] - x[i]
        area = dx * y[i]
        result += area
        print(f"Step {i+1}: ({x[i+1]} - {x[i]}) * {y[i]} = {area}")

    print(f"\nFinal Result: {result}")

    return result