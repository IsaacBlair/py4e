#This program records the domain name (instead of the
#address) where the message was sent from instead of
#who the mail came from (i.e., the whole email
#address). At the end of the program, print out the
#contents of your dictionary.

text = input('Enter a file name: ')
file = open(text)
counts = dict()

for line in file :
    if line.startswith('From ') :
        words = line.split()
        for word in words :
            if '@' in word :
                stripped = word.strip()
            else :
                continue
        day = words[1]
        at = stripped.index('@')
        email = day[at:]
        counts[email] = counts.get(email, 0) + 1

print(counts)
