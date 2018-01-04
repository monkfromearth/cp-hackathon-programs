from itertools import combinations_with_replacement as c
for _ in xrange(input()):
    o,n=map(int,raw_input().split())
    p=map(int,raw_input().split())
    if all(s > o for s in p):
        print "NO"; continue
    p = [pk for pk in p if pk <= o]
    r=map(len,[s for i in range(n,0,-1) for s in c(p, i) if sum(s)==o])
    k=min(r) if len(r) > 0 else 0
    print k if k != 0 else "NO"