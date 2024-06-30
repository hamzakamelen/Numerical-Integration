print("""
      ===== Simpson's 3/8 Rule =====
     Formula:
     ∫ydx= 3h/8 (y0+2(y3+y6+...+yn-3)+3(y1+y2+y4+y5+...+yn-2+yn-1)+yn)
    
    Choose Any One
      1. Find Numerical Integration for x and f(x) 
      2. Find Numerical Integration for f(x) = `Equation` and Step Value `h`  
      """)
option = int(input("Choose Any One Option ")) 
if(option==1):
      ValuesofXSt = input("Write Values of `x` (You can use , as a seperator) \n")
      splitinput= ValuesofXSt.split(",")
      if len(splitinput)%3 != 0:
          ValuesofX = [float(x) for x in splitinput]
      else:
          raise ValueError("Interval must be `Multiple of 3`") 
      ValuesofFxSt = input("Write Values of `f(x) or y` (You can use , as a seperator) \n")
      splitinput2= ValuesofFxSt.split(",")
      if len(splitinput2)%3 != 0 and len(splitinput) == len(splitinput2):
          ValuesofFx = [float(x) for x in splitinput2]
      else:
            raise ValueError("Interval must be Equal to Length of x")
      SumOfMultipleof3 = 0
      SumOfRemaining = 0
      h = (ValuesofX[1] - ValuesofX[0])
      
      for i in range(1,len(ValuesofFx)-1):
            if(i%3==0):
                  SumOfMultipleof3 += ValuesofFx[i]
            else:
                  SumOfRemaining += ValuesofFx[i]
      print(f"∫ydx= 3x{h}/8 ({ValuesofFx[0]}+2({SumOfMultipleof3})+3({SumOfRemaining})+{ValuesofFx[-1]})")
      Answer = (3*h/8)*(ValuesofFx[0]+2*SumOfMultipleof3+3*SumOfRemaining+ValuesofFx[-1])
      Result = round(Answer,3) 
      print("∫ydx=",Result)  
      print(f"Solution by Simpson's 3/8 Rule is {Result}")

if(option==2):
      ValueofFxSt = input("Enter Value of `f(x)`")
      try:
            ValueofFx = eval(ValueofFxSt)  # Convert string to function object (if possible)
      except SyntaxError:
            print("Invalid function")
      Valueofa = input("Enter Value of `a`")
      Valueofb = input("Enter Value of `b`")
      Interval = int(input("Enter no of Interval `n` (Must be Multple of three)"))
      if(Interval % 3 == 0 ):
            raise ValueError("Interval Must be Multiple of 3")
      
      
      