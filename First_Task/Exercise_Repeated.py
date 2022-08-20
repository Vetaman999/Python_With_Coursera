hrs = input('Enter Hours:')
pay = input('Enter Pay:')

hrs = float(hrs)
pay = float(pay)

if hrs > 40:
    pah = hrs * pay
    pag = (hrs - 40) * (pay * 0.5)
    xp = pah + pag
else:
    xp = hrs * pay

print('Pay:', xp)