#  Write a Python program to get the Fibonacci series of given range.

num = int(input("Enter the number for Fibonacci series: "))

a, b = 0, 1

print("Fibonacci series:")
for _ in range(num):
    print(a, end=" ")
    a, b = b, a + b