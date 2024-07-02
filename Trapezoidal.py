import numpy as np


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = h * (0.5 * y[0] + 0.5 * y[-1] + np.sum(y[1:-1]))
    return result


def trapezoidal_rule_discrete(x, Fx):
    if len(x) != len(Fx):
        raise ValueError("Length of x and Fx must be equal.")

    h = x[1] - x[0]  # Assuming uniform spacing

    print("""Formula:
    ∫ydx = h/2 (y0 + 2(y1 + y2 + ... + yn-1) + yn)""")
    print(f"({h}/2)*({Fx[0]} + 2 x {sum(Fx[1:-1])} + {Fx[-1]})")

    result = (h / 2) * (Fx[0] + 2 * sum(Fx[1:-1]) + Fx[-1])
    rounded_result = round(result, 3)

    print("∫ydx = ", rounded_result)
    print(f"Solution by Trapezoidal Rule is {rounded_result}")

    return rounded_result


def trapezoidal_rule_interactive():
    print(""" ===== Trapezoidal Rule =====
    Formula:
    ∫ydx = h/2 (y0 + 2(y1 + y2 + ... + yn-1) + yn)
    Choose Any One
    1. Find Numerical Integration for x and f(x)
    2. Find Numerical Integration for f(x) = `Equation` and Step Value `h`""")

    option = int(input("Choose Any One Option "))

    if option == 1:
        ValuesofXSt = input("Write Values of `x` (You can use , as a separator) \n")
        ValuesofX = [float(x) for x in ValuesofXSt.split(",")]

        ValuesofFxSt = input("Write Values of `f(x) or y` (You can use , as a separator) \n")
        ValuesofFx = [float(x) for x in ValuesofFxSt.split(",")]

        return trapezoidal_rule_discrete(ValuesofX, ValuesofFx)

    elif option == 2:
        ValueofFxSt = input("Enter Value of `f(x)`: ")
        try:
            ValueofFx = lambda x: eval(ValueofFxSt)
        except SyntaxError:
            print("Invalid function")
            return None

        Valueofa = float(input("Enter Value of `a`: "))
        Valueofb = float(input("Enter Value of `b`: "))

        if Valueofa >= Valueofb:
            raise ValueError("Lower bound must be less than upper bound.")

        Interval = int(input("Enter no of Interval `n`: "))
        h = (Valueofb - Valueofa) / Interval

        x = np.linspace(Valueofa, Valueofb, Interval + 1)
        Fx = [round(ValueofFx(xi), 3) for xi in x]

        print("Values of X is ", x.tolist())
        print("Values of f(X) is ", Fx)

        return trapezoidal_rule_discrete(x, Fx)

    else:
        print("Invalid option selected.")
        return None



if __name__ == "__main__":
    trapezoidal_rule_interactive()