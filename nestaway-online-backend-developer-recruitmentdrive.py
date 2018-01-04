for _ in xrange(input()):
    l = input(); n = sorted(map(int, raw_input().split())); k = {}
    for i in n:
        c = (bin(i)[2:]).count('1')
        k[c] = i if k.get(c,i) >= i else k.get(c)
    print ' '.join(map(str, k.itervalues()))