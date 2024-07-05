def simpson_1_3(x, Fx, h):
    # Takes x and Fx in List Data Type
    if len(x) != len(Fx):
        raise ValueError("Length of x and Fx must be equal.")
    SumOfEven = 0
    SumOfOdd = 0
    for i in range(1, len(Fx) - 1):
        if (i % 2 == 0):
            SumOfEven += Fx[i]
        else:
            SumOfOdd += Fx[i]
    print("""Formula:
    ∫ydx= (h/3) (y0+4(y1+y3+...+yn-1)+2(y2+y4+...+yn-2)+yn)""")
    print(f"∫ydx = (h/3) ({Fx[0]}+4({SumOfOdd})+2({SumOfEven})+{Fx[-1]})")
    Answer = (h / 3) * (Fx[0] + 4 * SumOfOdd + 2 * SumOfEven + Fx[-1])
    Result = round(Answer, 3)
    print("∫ydx = ", Result)
    print(f"Solution by Simpson's 1/3 Rule is {Result}")

print("""
===== Simpson's 1/3 Rule =====
Formula:
∫ydx= (h/3) (y0+4(y1+y3+...+yn-1)+2(y2+y4+...+yn-2)+yn)
Choose Any One
1. Find Numerical Integration for x and f(x)
2. Find Numerical Integration for f(x) = `Equation` and Step Value `h`
""")
option = int(input("Choose Any One Option "))

if (option == 1):
    ValuesofXSt = input("Write Values of `x` (You can use , as a seperator) \n")
    splitinput = ValuesofXSt.split(",")
    if len(splitinput) % 2 != 0:
        ValuesofX = [float(x) for x in splitinput]
    else:
        raise ValueError("Interval must be `Even`")

    ValuesofFxSt = input("Write Values of `f(x) or y` (You can use , as a seperator) \n")
    splitinput2 = ValuesofFxSt.split(",")
    if len(splitinput2) % 2 != 0 and len(splitinput) == len(splitinput2):
        ValuesofFx = [float(x) for x in splitinput2]
    else:
        raise ValueError("Interval must be Equal to Length of x")

    h = (ValuesofX[1] - ValuesofX[0])
    simpson_1_3(ValuesofX, ValuesofFx, h)

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
        Interval = int(input("Enter no of Interval `n` (Must be Even)"))
        if (Interval % 2 != 0):
            raise ValueError("Interval Must be Even")
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
        simpson_1_3(x, Fx, h)