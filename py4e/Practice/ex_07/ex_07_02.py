spam = 0
lines = 0

try:
    fhand = open(input('Enter a file name:'))
except:
    print('That file name does not exist.')
    quit()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        line = line.rstrip()
        stripped = line.strip('X-DSPAM-Confidence: ')
        spam = spam + float(stripped)
        lines = lines + 1
    else:
        continue
print('Average spam confidence:', spam/lines)
