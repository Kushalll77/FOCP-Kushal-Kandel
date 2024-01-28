
# 1.Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.



def greet(name):
    if name == '':
        return "Hello, Stranger!"
    else:
        return f"Hello, {name}!"

name = input("Please enter your name: ")
print(greet(name))
print()


# 2.Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.

# In[19]:


def passwords(password1,password2):
    if password1 == password2:
        return "Password Set"
    else:
        return"Error"
    
password1=input("Please enter your new password:")
password2=input("Please confirm your newpassword:")
              
print(passwords(password1,password2))
print()


# 3.Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.

# In[25]:


def passwords(password1,password2):
    if password1 == password2:
        if 8 <= len(password1) <= 12:
            return "Password Set"
        else:
            return "Password length must be between 8 and 12 characters. Please try again."
    else:
         return "Passwords do not match. Please try again."
    
password1=input("Please enter your new password:")
password2=input("Please confirm your new password:")
              
print(passwords(password1,password2))
print()


# 4.Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# 
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# In[39]:


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

def passwords(password1,password2):
    if password1 == password2:
        if 8 <= len(password1) <= 12: 
            if password1.lower() not in BAD_PASSWORDS:
                return"Password Set"
            else:
                return "Your chosen password is too common. Please try again."
        else:
            return "Password length must be between 8 and 12 characters. Please try again."
    else:
        return "Passwords do not match. Please try again."

           

password1 = input("Please enter your new password: ")
password2 = input("Please confirm your new password: ")

print(passwords(password1, password2))
print()


# 5.Modify your program a final time so that it executes until the user successfully
# chooses a password. That is, if the password chosen fails any of the checks, the
# program should return to asking for the password the first time.



common_passwords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password = input("Please enter a password between 8 and 12 characters long: ")

    if len(password) < 8 or len(password) > 12:
        print("Invalid password length. Please try again.")
        continue

    if password in common_passwords:
        print("That password is too common. Please choose another one.")
        continue

    print("Hello, your password is set!")
    break
print()


# 6.Write a program that displays the "Seven Times Table". That is, the result of
# multiplying 7 by every number from 0 to 12 inclusive. The output might start:**
# 
# 0 x 7 = 0
# 
# 1 x 7 = 7
# 
# 2 x 7 = 14 and so on.


for i in range(13):
    print(f"{i} x 7 = {i*7}")

print()


# 7.Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive.



def times_table(a):
    if a < 0 or a> 12:
        print("Please enter a number between 0 and 12.")
    else:
        for i in range(13):
            print(f"{i} x {a} = {i*a}")

a= int(input("Enter the number : "))
times_table(a)
print()


# 8.Modify the "Times Table" again so that the user still enters the number of the table,
# but if this number is negative the table is printed backwards. So entering "-7"
# would produce the Seven Times Table starting at "12 times" down to "0 times".


def times_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))

if num < 0:
    # Reverse the range of the loop
    for i in range(10, 0, -1):
        print(f"{num} x {i} = {num * i}")
else:
    times_table(num)