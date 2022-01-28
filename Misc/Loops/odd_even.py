i = range (1,10)
odd = 0
even = 0
for x in i:
    if x % 2 == 0 :
        even = even + 1
    else:
        odd = odd + 1
print('Number of odd numbers: ',odd)
print('Number of even numbers: ',even)
