#this program calculates factorial using user defined method

def findfact(n):
    s = 1  # initialisation statement
    for i in range(1, n + 1):  # loop using range function
        s = s * i
    return(s)



n=int(input("Enter a number"))
s=findfact(n)
print(s)
