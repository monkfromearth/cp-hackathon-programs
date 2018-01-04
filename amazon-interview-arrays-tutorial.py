from collections import Counter
from math import hypot

def getShape(pos_of_1s):
    (x1,y1), (x2,y2), (x3,y3), (x4,y4) = pos_of_1s
    x2 -= x1; x3 -= x1; x4 -= x1; y2 -= y1; y3 -= y1; y4 -= y1; x1 = 0; y1 = 0;
    condition = (x2 + x3 == x4 and y2 + y3 == y4 and x2 * x3 == -y2 * y3) or \
                (x2 + x4 == x3 and y2 + y4 == y3 and x2 * x4 == -y2 * y4) or \
                (x3 + x4 == x2 and y3 + y4 == y2 and x3 * x4 == -y3 * y4)
    if condition:
        d2 = hypot(x2,y2)
        d3 = hypot(x3,y3)
        d4 = hypot(x4,y4)
        cond_for_square = False
        if d2 == d3:
            d = hypot(x2-x4, y2-y4)
            cond_for_square = (d == hypot(x3-x4, y3-y4) and d == d2)
        if d3 == d4:
            d = hypot(x2-x3, y2-y3);
            cond_for_square =  (d == hypot(x2-x4, y2-y4) and d == d3);
        if d2 == d4:
            d = hypot(x2-x3, y2-y3);
            cond_for_square = (d == hypot(x3-x4, y3-y4) and d == d2);
        return "square" if cond_for_square else "rectangle"
    else:
        return "triangle"

for _ in xrange(input()):
    arr, started, count, n = [], False, 0, input()
    for __ in xrange(n):
        inp = list(raw_input())
        c = Counter(inp).get('1', 0)
        if (c is not 0) or (0 < count < 4): started = True
        if count >= 4: started = False
        count += c
        if started: arr += [ inp ]
        pos_of_1s = []
        for r in xrange(len(arr)):
            for c in xrange(n):
                if arr[r][c] is '1':
                    pos_of_1s += [ (r,c) ]
    print getShape(pos_of_1s)