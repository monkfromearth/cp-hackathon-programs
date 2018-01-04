from collections import Counter

def get_bin(x):
    return bin(x)[2:]
    
def is_special_number(x):
    
    # Condition a
    if all(map(int,list(x))):
        return True
        
    # Condition b & c
    """ Gettings bits """
    bits = []
    c = Counter(x)
    c1, c0 = c['1'], c['0']
    i1 = [i for i, a in enumerate(x) if a == '1']
    i0 = [i for i, a in enumerate(x) if a == '0']
    current_bit = None
    current_count = 0
    for i in xrange(len(x)):
        if i in i0:
            if current_bit is None:
                current_bit = 'U'
                current_count = 1
            elif current_bit is 'S':
                bits += [ ('S', current_count) ]
                current_count = 1
                current_bit = 'U'
                if i == (len(x)-1):
                    bits += [ ('U', current_count) ] 
            elif current_bit is 'U':
                current_count += 1
                if i == (len(x)-1):
                    bits += [ ('U', current_count) ]    
        elif i in i1:
            if current_bit is None:
                current_bit = 'S'
                current_count = 1
            elif current_bit is 'U':
                bits += [ ('U', current_count) ]
                current_count = 1
                current_bit = 'S'
                if i is (len(x)-1):
                    bits += [ ('S', current_count) ]
            elif current_bit is 'S':
                current_count += 1
                if i is (len(x)-1):
                    bits += [ ('S', current_count) ]    
    """ Evaluating order from bits """
    status = False
    last_count = 0
    for b in bits:
        if b[0] == 'S':
            if b[1] > last_count:
                status = True
                last_count = b[1]
            else :
                status = False
                break
    return status

for _ in xrange(input()):
    a,b = map(int, raw_input().split())
    c = []
    for i in xrange(a,b+1):
        l = get_bin(i)
        if is_special_number(l):
            c += [i]
    print len(c)