biggest = None
print ('Before')
for i in [9,41,12,3,74,15] :
    if biggest is None :
        biggest = i
    elif i > biggest :
        biggest = i
print('Result: ', biggest)
