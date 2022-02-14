#Write a program that reads a file and prints the letters in decreasing order of
#frequency. Your program should convert all the input to lower case and only
#count the letters a-z. Your program should not count spaces, digits,
#punctuation, or anything other than the letters a-z. Find text samples from
#several different languages and see how letter frequency varies between
#languages. Compare your results with the tables at
#https://wikipedia.org/wiki/Letter_frequencies.

text = input('Enter a file name: ')
file = open(text)
counts = dict()

alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
count = 0

for line in file :
    line = line.lower()
    line = line.split()
    for word in line :
        for letter in word :
            if letter in alphabet :
                counts[letter] = counts.get(letter, 0) + 1

lst = list()

for letter, count in counts.items() :
    newtup = (count, letter)
    lst.append(newtup)

result = sorted(lst, reverse = True)

for count, letter in result :
    print(letter)
