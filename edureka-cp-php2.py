for _ in xrange(input()):
    n = input()
    arr1 = sorted(map(int,raw_input().split()))
    arr2 = sorted(map(int,raw_input().split()))
    if arr1 == arr2 : print "Yes"
    else :
        arr = arr2[:]
        for e in arr1:
            if e in arr: arr.remove(e)
        if len(arr) == 1:
            sum1 = sum(arr1); sum2 = sum(arr2)
            arr = 2 if sum1 > sum2 else 1
            add = abs(sum1 - sum2)
            print "%d %d" % (add, arr)
        else: print "No"