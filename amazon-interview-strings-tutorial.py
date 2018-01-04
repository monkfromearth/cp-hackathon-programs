for _ in xrange(input()):
    
    s1, s2 = [ list(raw_input()) for _ in [0,1] ]
    
    cl = list(set(s1).intersection(s2))
    
    #print cl
    
    sh, lg = (s2, s1) if len(s1) > len(s2) else (s1, s2)
    
    s1 = [ x for x in s1 if x in cl ]
    s2 = [ x for x in s2 if x in cl ]
    
    sh, lg = (s2, s1) if len(s1) > len(s2) else (s1, s2)
    
    #print "sh: ", sh
    #print "lg: ", lg
    
    char = []
    chars = []
    k = []
    
    if sh != lg:

        temp_sh = sh[:]
        temp_lg = lg[:]

    #    print "\nStarting the loop ...\n"
    
        for c_sh in sh:
        
    #        print "Character in sh: %c" % (c_sh)
        
            highest_index = 0
            added = False
                
            if len(lg) > 0:
                
                for i in xrange(len(lg)):
            
                    c_lg = lg[i]
            
    #                print "Character in lg: %c at index %d" % (c_lg, i)
                
                    if c_sh is c_lg:
                        char += [ c_sh ]
                        highest_index = i
                        added = True
                        break
            
    #        print "Highest Index: %d" % (highest_index)    
            
    #        print "lg (before): ", lg
            
            
            if added:
                for _ in xrange(highest_index+1):
                    if len(lg) > 0:
                        lg.pop(0)
    #                    print "Removed char: ", lg.pop(0)
            
    #        print "lg (after): ", lg
    #        print "char: ", char
    #        print ""
            
            k = char
    
    #    print "\nLoop terminated!\n"
        
        chars += [ ''.join(char) ]
        char = [][:]
        
        sh = temp_sh[:]
        lg = temp_lg[:]
        
    #    print sh, lg
        
    #    print "\nStarting the loop ...\n"
    
        for c_lg in lg:
        
    #        print "Character in lg: %c" % (c_lg)
        
            highest_index = 0
            added = False
        
            if len(sh) > 0:
            
                for i in xrange(len(sh)):
            
                    c_sh = sh[i]
            
    #                print "Character in sh: %c at index %d" % (c_sh, i)
            
                    if c_sh is c_lg:
                        char += [ c_lg ]
                        highest_index = i
                        added = True
                        break
            
    #        print "Highest Index: %d" % (highest_index)    
            
    #        print "sh (before): ", sh
            
            if added:
                for _ in xrange(highest_index+1):
                    if len(sh) > 0:
                        sh.pop(0)
    #                    print "Removed char: ", sh.pop(0)
            
    #        print "sh (after): ", sh
    #        print "char: ", char
    #        print ""
            
    #    print "\nLoop terminated!\n"
        
        chars += [ ''.join(char) ]
        char = [][:]
            
    #    print "chars: ", chars
            
        k = sorted(chars, key=len)[-1]
    
    else :
        
        k = sh
    
    print ''.join(k) if len(k) > 0 else "NO STRING DERIVED" 
    #print "___________________________________\n" 