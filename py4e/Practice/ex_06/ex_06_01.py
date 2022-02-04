#Write a while loop that starts at the last character in the string and
#works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
fruit = 'My Arrakis, My DUNE'
length = int(len(fruit))
while length > 0 :
    print (fruit[length - 1])
    length = length - 1
