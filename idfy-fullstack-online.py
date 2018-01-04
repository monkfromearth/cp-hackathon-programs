from datetime import timedelta as td
from operator import itemgetter
from itertools import groupby

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

def assign_server(i,t,end=False,sn=0):
    if not end:
        for j in xrange(4):
            if s[j] is not "A":
                end = td(hours=t[0],minutes=t[1])
                prev_end = ss[j]['end']
                if len(prev_end) is 0:
                    s[j] = "A"
                    ss[j]['start'] += [ t ]
                    return j
                else :
                    l = ss[j]['end'][len(prev_end)-1]
                    start = td(hours=l[0],minutes=l[1])
                    if int((end-start).total_seconds()/60) >= 5:
                        s[j] = "A"
                        ss[j]['start'] += [ t ]
                        return j
                    else :
                        continue
    else :
        s[sn] = "IA"
        ss[sn]['end'] += [ t ]
        return sn

items = input()

ts = []
tl = []
tts = {'start':[], 'end':[]}
s = {}
ss = {}
serv = {}
sss = []

for i in xrange(items):
    s[i] = "IA"
    ss[i] = {'start':[],'end':[]}
    serv[i] = 0

for _ in xrange(items):
    inp = map(int, raw_input().split())
    ts += [[(inp[0], inp[1]), (inp[2], inp[3])]]
    tl += [(inp[0], inp[1]),(inp[2], inp[3])]
    
for i in xrange(len(ts)):
    t = ts[i]
    tts['start'] += [ t[0] ]
    tts['end'] += [ t[1] ]
    
tl = list(set(tl))    
    
tl = [ td(hours=t[0],minutes=t[1]).total_seconds() for t in tl ]
tl.sort()
tl = [ (int(divmod(divmod(t,60)[0],60)[0]),int(divmod(divmod(t,60)[0],60)[1])) for t in tl ]

ts = sorted(ts,key=lambda x:x[1][0])

for t in tl:
    #print "Timestamp: ", t
    #for i in xrange(items):
    #    print "Server #%d : " % i, s[i]
    st = list_duplicates_of(tts['start'], t)
    en = list_duplicates_of(tts['end'], t)
    for i in st:
        k = assign_server(i,t)    
        serv[i] = k
    for i in en:
        assign_server(i,t,True,serv[i])
    m = 0
    for i in xrange(len(s)):
        if s[i] is "A":
            m = i
    sss += [ m+1 ]
    #print ""
print max(sss)