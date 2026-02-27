# Stage 2: Add Result Check

# Extend Stage 1: After showing result, check if it's positive, negative, or zero and print accordingly.

x,y,z=(input("Enter two numbers and arithmetic operation(+,-,*,/) as comma separated values (eg: 10,20,+)").split(","))

def value():
    if Result > 0:
        print("Positive Value")
    elif Result < 0:
        print("Negative Value")
    elif Result == 0:
        print("Zero Value")
        
if z=="+":
    Result=int(x)+int(y)
    print("Result=", Result)
    value()
elif z=="-":
    Result=int(x)-int(y)
    print("Result=", Result)
    value()
elif z=="*":
    Result=int(x)*int(y)
    print("Result=", Result)
    value()
elif z=="/":
    if int(y)==0:
        print("Division by Zero is not allowed")
    else:
        Result=int(x)/int(y)
        print("Result=", Result)  
        value()
else:
    print("Enter the inputs in correct format")
