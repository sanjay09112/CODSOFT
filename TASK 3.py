import random
import string
def genrate_password(length):
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    punctuation=string.punctuation
    digits=string.digits
    
    all=lowercase+uppercase+punctuation+digits
    password=''.join(random.choice(all) for _ in range(length))
    return password
print('Welcome to password generator')
while True:
    try:
        length=int(input("Enter the length you want to generate password:"))
        if(length<0):
            print("Invalid input.Please enter positive number")
        else:
            break
    except ValueError:
        print("Invalid input.Enter a integer")
password=genrate_password(length)
print("Your generated password is:",password)