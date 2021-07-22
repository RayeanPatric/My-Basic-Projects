sd1 = 50000

print('your default standard deduction is Rs. 50000')

ti = int(input('\nEnter your total income :Rs.'))
ti1 = ti - sd1
print('\nafter cancelling sd amt.: Rs.', ti1)

ct = int(input('\nEnter your co-operation amt.:Rs.'))
ti2 = ti1 - ct
print('\nafter gross total income amt.: Rs.', ti2)

sa1 = int(input('\nEnter your GPF amt.:Rs.'))
sa2 = int(input('\nEnter your child tution fee.:Rs.'))
sa3 = int(input('\nEnter your LIC amt.:Rs.'))
sa4 = int(input('\nEnter you Housing loan principal amt.:Rs.'))
sa = sa1 + sa2 + sa3 + sa4
if sa >= 150000:
    sa = 150000
ti3 = (ti2 - sa)
print('\nafter savings amt.: Rs.', ti3)

hi = int(input('\nEnter your housing loan Intrest amt.:Rs.'))
if hi >= 200000:
    hi = 200000
ti4 = (ti3 - hi)
print('\nafter savings amt.: Rs.', ti4)
mc = int(input('\nEnter your medi - care amt.:Rs.'))
ti5 = ti4 - mc
print('\nafter medicare amt.: Rs.', ti5)

ce = int(input('\nEnter you special child exception amt.:Rs.'))
ti6 = ti5 - ce
print('\ntotal income : Rs.', ti6)

if ti6 <= 250000:
    print('0')
elif 250000 < ti6 < 500001:
    ti7 = ti6 - 250000
    if ti7 > 250000:
        ti8 = ti7 - 250000
        ti9 = 0.05 * ti8
        if ti8 > 250000:
            ti10 = ti8 - 250000
            ti11 = 0.2 * ti10
            ftx = (ti9 + ti11) + ((ti9 + ti11) * 0.04)
            print('\nyour total taxable amt.:', ftx)
        else:
            ftx = ti9 + (ti9 * 0.04)
            print('\nyour total taxable amt.:', ftx)

elif 500000 < ti6 < 1000001:
    ti7 = ti6 - 250000
    if ti7 > 250000:
        ti8 = ti7 - 250000
        tx = 0.2 * ti8
        if ti8 > 250000:
            ti9 = ti8 - 250000
            tx1 = 0.3 * ti9
            ftx = (tx + tx1) + (((tx + tx1) * 0.04) + 12500)
            print('\nyour total taxable amt.:', ftx)
        else:
            ftx = (tx + 12500 + (tx * 0.04))
            print('\nyour total taxable amt.:', ftx)

else:
    ti7 = ti6 - 1000000
    ti8 = (ti7 * 0.3)
    ti9 = ti8 * 0.04
    ftx = (ti8 + ti9 + 112500)
    print('\nyour total taxable amt.:', ftx)

at = int(input('\nEnter the advance tax paid : Rs. '))

ft = ftx - at

if ft < 0:
    print('\nthe amt. to be returned to you is Rs. ', (-1 * ft))
elif ft == 0:
    print('\nthe amt. to be paid by you is Rs. 0')
else:
    if 0 < ft < 1:
        ft = 0
        print('\nthe amt to be paid by you is Rs. ', ft)

e = input('\npress ENTER to exit')
