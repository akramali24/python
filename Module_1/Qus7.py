#  Write a Python program to find whether a given number is even or odd,print out an appropriate message to the user.

n = int(input("Enter number :"))

if n % 2 == 0:
    print("Even number :",n)
else:
    print("Odd number :",n)