grade = input('Enter score: ')
try:
    grade = float(grade)
except:
    print('Bad score')
    quit()
if grade > 1 :
    print('Bad score')
elif grade >= .9 :
    print('A')
elif grade >= .8 :
    print ('B')
elif grade >= .7 :
    print ('C')
elif grade >= .6 :
    print ('D')
elif grade < .6 :
    print('F')
