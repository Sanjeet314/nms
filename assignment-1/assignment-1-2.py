# 2.Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.

def reversename(firstname, lastname):
    fullname = firstname + " " + lastname
    return fullname[::-1]

firstName = input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")

print(reversename(firstName, lastName))

