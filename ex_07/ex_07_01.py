try:
    fhand = open(input('Enter a file name:'))
except:
    print('That file name does not exist.')
    quit()
for line in fhand:
    line = line.rstrip()
    print(line.upper())
