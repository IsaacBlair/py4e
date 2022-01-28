sum = 0.0
count = 0
average = None
while True:
    svalue = input('Enter a number:')
    if svalue == 'done' :
        break
    try :
        value = float (svalue)
    except :
        print('Invalid input')
        continue
    count = count + 1
    sum = sum + value
    average = sum/count
    #print(value)
print('Done!')
print(sum, count, average)
