#Write a simple program to simulate the operation of the grep command on Unix.
#Ask the user to enter a regular expression and count the number of lines that
#matched the regular expression:

import re
grep = input('Enter a regular expression: ')
count = 0

file = open('mbox.txt')
for line in file :
    line = line.rstrip()
    if re.search(grep, line):
        count = count + 1

print('mbox.txt had ',count,' lines that matched ',grep)
