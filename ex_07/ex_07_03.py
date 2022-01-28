lines = 0

try:
    fname = input('Enter a file name:')
    fhand = open(fname)
except:
    print('That file name does not exist.')
    quit()
for line in fhand:
    if line.startswith('Subject:'):
        #line = line.rstrip()
        lines = lines + 1
    else:
        continue
print('There were',lines,'subject lines in',fname)
