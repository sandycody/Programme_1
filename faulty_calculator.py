""" Design a calculator which will correctly solve all the problems except the following
    ones:  45*3= 555,56+9= 77,56/6= 4
    Your programme should take operator and the two numbers as input from the user and
    then return the result. """


# Solution 

print("WELCOME TO THE CALCULATOR:")
print("\nList of operators as follows:")
print("* for Multiplication")
print("+ for Addition")
print("/ for Division")
op=input("Enter an operator: ")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if(op=="*"):
    res=num1*num2
    if((num1==45)&(num2==3)):
        res=555
        print("45*3 =",res)
    else:
        print("num1*num2 =",num1*num2)
elif(op=="+"):
    res=num1+num2
    if((num1==56)&(num2==9)):
        res=77
        print("56+9 =",res)
    else:
        print("num1+num2 =",num1+num2)
elif(op=="/"):
    res=num1//num2
    if ((num1==56)&(num2==6)):
        res=4
        print("56/6 =",res)
    else:
        print("num1/num2 =",num1//num2)
else:
    print("Sorry! This operator is not in the list.")

print("\nThank you for using the calculator.")