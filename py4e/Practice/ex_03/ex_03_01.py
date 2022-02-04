xh = float(input('Enter Hours:'))
xr = float(input('Enter Rate:'))
if xh > 40 :
  xp = 40 * xr + (xh - 40) * (1.5 * xr)
else :
  xp = float(xh) * float(xr)
print ('Pay:', xp)
