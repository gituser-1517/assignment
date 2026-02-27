# Stage 1: Basic Calculator
# Create a calculator that takes two numbers and an operator (+, -, *, /) and shows the result.

# Constraints:

# Handle division by zero
# Use if-elif-else statements


x,y,z=(input("Enter two numbers and arithmetic operation(+,-,*,/) as comma separated values (eg: 10,20,+)").split(","))
if z=="+":
   print("Result=", int(x)+int(y))
elif z=="-":
    print("Result=", int(x)-int(y))
elif z=="*":
    print("Result=", int(x)*int(y))
elif z=="/":
    if int(y)==0:
        print("Division by Zero is not allowed")
    else:
        print("Result=", int(x)/int(y))
else:
    print("Enter the inputs in correct format")
