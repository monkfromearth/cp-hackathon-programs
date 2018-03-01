for _ in xrange(input()):
    n,c = map(int, raw_input().split())
    plots = map(int, raw_input().split())
    arth = c*n - sum(plots)
    arth2 = 0
    new_plots = []; current_plot = []
    for plot in plots:
        if plot <= c: current_plot += [plot]
        else:
            if len(current_plot) == 0: continue
            else:
                new_plots += [ current_plot ]
                current_plot = []
    if len(current_plot) != 0: new_plots += [ current_plot ]
    if len(new_plots) == 0: print 0
    else:
        p = max(new_plots)
        arth2 = c*len(p) - sum(p)
    print max([arth, arth2])