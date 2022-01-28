xh = input('Enter Hours:')
try:
    xhf = float(xh)
except:
        print('Error, please enter numeric input')
        quit()
xr = input('Enter Rate:')
try:
    xrf = float(xr)
except:
        print('Error, please enter numeric input')
        quit()
if xhf > 40 :
  xpf = 40 * xrf + (xhf - 40) * (1.5 * xrf)
else :
  xpf = float(xhf) * float(xrf)
print ('Pay:', xpf)
