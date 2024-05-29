# Write a Python program to test whether a passed letter is a vowel or not.

ch = input("Enter letter :")

ch = ch.lower()

vowel = 'a', 'e', 'i', 'o', 'u'
 
if ch is vowel:
    print("This is vowel :",ch)
else:
    print("This is not vowel")