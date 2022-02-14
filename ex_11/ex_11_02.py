import re

file = open(input('Enter file:'))
count = 0
lst = list()

for line in file :
    line = line.rstrip()
    x = re.findall('New Revision:.([0-9]+)', line)
    if len(x) > 0:
        for i in x:
            i = int(i)
            lst.append(i)
            average = sum(lst)/len(lst)
print(int(average))
