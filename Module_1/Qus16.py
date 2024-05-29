# Write a Python program to count the occurrences of each word in a given sentence 

sentence="this is a python"
sentence=sentence.split()
i=0
count=0
while i<len(sentence):
    count=0
    for j in sentence:
        if sentence[i]==j:
             count+=1
    print('Sentence in each word are count :',sentence[i],":",count)
    i+=1
