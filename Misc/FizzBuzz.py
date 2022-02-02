#for numbers between 1 and 45 if the number is divisble by 3 print Fizz, if the number is divisble by 5 print Buzz, if the number is divisible by 3 and 5 print FizzBuzz

for i in range (1,46) :
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0 :
        print('Fizz')
    elif i % 5 == 0 :
        print('Buzz')
    else :
        print(i)
