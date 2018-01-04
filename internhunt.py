"""def findw(o, w):
    w = [i for i in w if i <= o]
    if len(w) is 0: return False
    if o in w: return True
    for c in w:
        n = o - c; w.remove(c)
        if findw(n, w): return True
    return False
    
for _ in xrange(int(raw_input().strip())):
    i = map(int, raw_input().strip().split(" "))
    n, w = i[0], i[1:]
    o = int(raw_input().strip())
    print "YES" if findw(o, w) else "NO"
    
---------------------------------------------------------------
"""
from itertools import combinations as c
for _ in xrange(input()):
    p = map(int,raw_input().split()[1:])
    o = input()
    if all(s > o for s in p):
        print "NO"; continue
    p = [pk for pk in p if pk <= o]
    r = [s for i in range(len(p),0,-1) for s in c(p, i) if sum(s)==o]
    print "YES" if len(r) > 0 else "NO"