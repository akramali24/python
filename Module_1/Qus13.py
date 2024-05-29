# Write a Python program to count the number of characters (character frequency) in a string.

string = "hello world"

for i in string:
    frequency = string.count(i)
    print(i,":",frequency,end=",")