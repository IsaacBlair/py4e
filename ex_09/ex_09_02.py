#Write a program that categorizes each mail message by
#which day of the week the commit was done. To do this
#look for lines that start with “From”, then look for
#the third word and keep a running count of each of
#the days of the week. At the end of the program
#print out the contents of your dictionary
#(order does not matter).


text = input('Enter a file name: ')
file = open(text)
counts = dict()

for line in file :
    if line.startswith('From ') :
        words = line.split()
        day = words[2]
        counts[day] = counts.get(day, 0) + 1

print(counts)
