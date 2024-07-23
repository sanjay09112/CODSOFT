print("                     CALCULATOR")
print("-----------------------------------------------------------")
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
def rem(a,b):
    c=a%b
    return c
def squ(a):
    c=a*a
    return c
def cub(a):
    c=a*a*a
    return c
while(1):
    print("1.Addition")
    print("2.Subtraction")
    print("3.multiplication")
    print("4.Division")
    print("5.Remainder")
    print("6.Square of a number")
    print("7.cube of a number")
    print("8.exit")
    i=input("Enter your choice:")
    if(i=='8'):
        print("You choose exit,good bye!")
        break
    if i in ['1', '2', '3', '4','5','8']:
        a= float(input("Enter first number: "))
        b= float(input("Enter second number: "))
        
        if(i=='1'):
            print("Addition of",a,"and",b,"is",add(a,b))
        elif(i=='2'):
            print("Subtraction of",a,"and",b,"is",sub(a,b))
        elif(i=='3'):
            print("Multiplication of",a,"and",b,"is",mul(a,b))
        elif(i=='4'):
            print("Division of",a,"and",b,"is",div(a,b))
        elif(i=='5'):
            print("Remainder of",a,"and",b,"is",rem(a,b))
    if i in ['6','7']:
        a= float(input("Enter first number: "))
        if(i=='6'):
            print("Square of",a,"is",squ(a))
        elif(i=='7'):
            print("Cube of",a,"is",cub(a))
    else:
        print("Invalid input. Please enter a number between 1 and 8.")