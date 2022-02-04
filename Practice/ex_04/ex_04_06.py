def computepay(h, r) :
    # print("In computepay", h, r)
    if h > 40 :
        pay = 40 * r + (h - 40) * (1.5 * r)
    else :
        pay = float(h) * float(r)
    # print('Returning', pay)
    return pay
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
xpf = computepay(xhf, xrf)
print ('Pay', xpf)
