#This program counts the distribution of the hour of the day for each of the
#messages. You can pull the hour from the “From” line by finding the time string
#and then splitting that string into parts using the colon character. Once you
#have accumulated the counts for each hour, print out the counts, one per line,
#sorted by hour as shown below.


text = input('Enter a file name: ')
file = open(text)
counts = dict()

for line in file :
    if line.startswith('From ') :
        words = line.split()
        time = words[5]
        striptime = time.rstrip()
        hour = striptime[:2]
        counts[hour] = counts.get(hour, 0) + 1

lst = list()
for hour, count in counts.items() :
    newtup = (hour, count)
    lst.append(newtup)
result = sorted(lst)

for hour, count in result :
    print(hour, count)
