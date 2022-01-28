sum = 0.0
count = 0
min = None
max = None
while True:
    svalue = input('Enter a number:')
    if svalue == 'done' :
        break
    try :
        value = int(svalue)
    except :
        print('Invalid input')
        continue
    count = count + 1
    sum = sum + value
    if min is None :
        min = value
    elif min > value :
        min = value
    if max is None :
        max = value
    elif max < value :
        max = value
print('Maximum is', max)
print('Minimum is', min)
