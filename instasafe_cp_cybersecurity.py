b = {'C':['C','A','B','O'],'A':['O','A'],'B':['O','B'],'O':['O']}
for _ in xrange(input()):
    cured = 0; c_q = list(raw_input()); p_q = list(raw_input())
    for p in p_q:
        needed = 3; perm = 0
        while True:
            if c_q[0] in b[p]:
                needed -= 1
                c_q.pop(0)
            else :
                c_q.append(c_q.pop(0))
                perm += 1
            if needed == 0:
                cured += 1
                break
            if perm == len(c_q):
                break
    print cured