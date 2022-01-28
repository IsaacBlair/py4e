str = 'X-DSPAM-Confidence:0.8475'
colon = int(str.find(':'))
numbers = float(str [colon + 1:])
print (numbers)
