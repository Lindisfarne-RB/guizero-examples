''' Create a multi operation calculator using two user entered numbers and an operator'''

''' operators as + ,- , * ,/ , modulus (%) using UDF '''

def sum (num1, num2):
    print("Sum of" ,num1 ,"and ",  num2, " is", num1+num2)




num1=int(input("Enter first num"))
num2=int(input("Enter second num"))

sum(num1,num2)