# simple calculator using python

print("CALCULATOR")
print("1 - ADD")
print("2 - SUBTRACT")
print("3 - MULTIPLY")
print("4 - DIVIDE")

option = int(input("choose your option to perform :"))

if(option in [1,2,3,4]):
    num1 = int(input("enter your first number :"))
    num2 = int(input("enter your second number :"))
    num3 = int(input("enter your third number :"))

    if(option == 1 ):
        result = num1 + num2 + num3 
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 // num2

else:
    print("your entered invalid operation")

print("your result :",result)
          

