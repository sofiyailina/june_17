f = open('9_9062.txt')
k = 0
for s in f:
    a = (int(x) for x in s.split())
    if (max(a) != a[-1]) and (min(a) != a[0]) \
            and ((max(a) - min(a)) % a[1]) == 0):
