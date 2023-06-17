for n in range(1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        summ = 0
        for d in b:
            summ += int(d)
        summ = str(summ%2)
        b = '1' + b + summ
    if n % 2 != 0:
        summ = 0
        for d in b:
            summ += int(d)
        summ = str(summ % 2)
        b = b + '0' + summ
    if int(b, 2) > 100:
        print(n)
        break


'''summ = 0
    for d in s:
        summ += int(d)'''