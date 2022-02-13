#Add code to the above program to figure out who has
#the most messages in the file. After all the data
#has been read and the dictionary has been created,
#look through the dictionary using a maximum loop
#(see Chapter 5: Maximum and minimum loops) to find
#who has the most messages and print how many messages
#the person has.

text = input('Enter a file name: ')
file = open(text)
counts = dict()

for line in file :
    if line.startswith('From ') :
        words = line.split()
        day = words[1]
        counts[day] = counts.get(day, 0) + 1

bigcount = None
bigword = None

for word, count in counts.items() :
    if bigcount is None or bigcount < count :
        bigcount = count
        bigword = word


print(bigword, bigcount)
