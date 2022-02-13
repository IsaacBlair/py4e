#Write a program to read through a mail log, build a
#histogram using a dictionary to count how many
#messages have come from each email address, and
#print the dictionary.

text = input('Enter a file name: ')
file = open(text)
counts = dict()

for line in file :
    if line.startswith('From ') :
        words = line.split()
        day = words[1]
        counts[day] = counts.get(day, 0) + 1

print(counts)
