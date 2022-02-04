#Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

words = list()
hi = list()
def chop(list) :
    list = list[1:-1]
def middle(list) :
    return list[1:-1]
while True :
    user = input('Enter a list of words, enter done when you are finished.')
    if user == 'done' :
        break
    list = hi.append(user)
chop = chop(hi)
middle = middle(hi)
print (chop)
print (middle)
