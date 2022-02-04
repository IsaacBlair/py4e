#download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.

romeo = open('romeo.txt')
words = list()
for line in romeo :
    line = line.split()
    for i in line :
        if i in words :
            continue
        else :
            words.append(i)
words.sort()
print(words)
