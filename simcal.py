print(
    '''
    + ADD
    - SUBTRACT
    * MULTIPLY
    / DIVIDE
    ''')
num1=eval(input("Enter a value1:-"))
num2=eval(input("Enter a value2:-"))
opr=input("Enter the opr..(+,-,/,*):-")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr == "/":
    print(num1/num2)
elif opr=="*":
    print(num1*num2)
else:
    print("Invalid input")

