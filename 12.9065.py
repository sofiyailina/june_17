for n in range(0, 1000):
    s = '>' + 21*'0' + '1'*n + '2'*11
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    summ = 0
    for d in s:
        summ += int(d)

    if summ % n == 0 :
        print(n)
        break