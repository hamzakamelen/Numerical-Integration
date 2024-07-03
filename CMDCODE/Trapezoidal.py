def trapezoidal_rule(x, Fx, h):
    # Takes x and Fx in List Data Type
    if len(x) != len(Fx):
        raise ValueError("Length of x and Fx must be equal.")
    print("""Formula:
    ∫ydx = h/2 (y0 + 2(y1 + y2 + ... + yn-1) + yn)""")
    print(f"({h}/2)*({Fx[0]} + 2 x {sum(Fx[1:-1])} + {Fx[-1]})")
    Answer = (h/2)*(Fx[0] + 2*sum(Fx[1:-1]) + Fx[-1])
    Result = round(Answer, 3)
    print("∫ydx = ", Result)
    print(f"Solution by Trapezoidal Rule is {Result}")

print(""" ===== Trapezoidal Rule =====
Formula:
∫ydx = h/2 (y0 + 2(y1 + y2 + ... + yn-1) + yn)
Choose Any One
1. Find Numerical Integration for x and f(x)
2. Find Numerical Integration for f(x) = `Equation` and Step Value `h`""")

option = int(input("Choose Any One Option "))

if (option == 1):
    ValuesofXSt = input("Write Values of `x` (You can use , as a seperator) \n")
    splitinput = ValuesofXSt.split(",")
    ValuesofX = [float(x) for x in splitinput]

    ValuesofFxSt = input("Write Values of `f(x) or y` (You can use , as a seperator) \n")
    splitinput2 = ValuesofFxSt.split(",")
    ValuesofFx = [float(x) for x in splitinput2]

    h = (ValuesofX[1] - ValuesofX[0])
    trapezoidal_rule(ValuesofX, ValuesofFx, h)

if (option == 2):
    ValueofFxSt = input("Enter Value of `f(x)`: ")
    try:
        ValueofFx = lambda x: eval(ValueofFxSt)  # Convert string to function object (if possible)
    except SyntaxError:
        print("Invalid function")

    Valueofa = int(input("Enter Value of `a`: "))
    Valueofb = int(input("Enter Value of `b`: "))

    if (Valueofa >= Valueofb):
        raise ValueError("Lower bound must be less than upper bound.")

    else:
        Interval = int(input("Enter no of Interval `n`"))
        h = (Valueofb - Valueofa) / Interval

        x = []
        Fx = []
        Starting = Valueofa
        i = 0
        while Starting <= Valueofb:
            x.append(Starting)
            Fx.append(round(ValueofFx(Starting), 3))
            Starting += h
            i += 1

        print("Values of X is ", x)
        print("Values of X is ", Fx)
        trapezoidal_rule(x, Fx, h)