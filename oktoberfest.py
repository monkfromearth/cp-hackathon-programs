def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    p = None
    for node in graph[start]:
        if node not in path:
            n = find_path(graph, node, end, path)
            if n:
                if not p or len(n) < len(p):
                    p = n
    return p

if __name__ == "__main__":
    for t in xrange(int(raw_input().strip())):
        n,m = map(int, raw_input().strip().split(" ")); allc, i, graph, money = [], 1, {}, False
        for mt in xrange(m):
            allc.append(tuple(map(int, raw_input().strip().split(" "))))
        while (i <= n):
            nodes = []
            for c in allc:
                if c[0] is i: nodes.append(c[1])
            nodes.sort(); graph.update({i:nodes}); i += 1
        i = 1
        while (i <= n):
            for j in xrange(1,n+1):
                if i != j:
                    path = find_path(graph, i, j)
                    if path is not None:
                        money = True if len(path) > 2 else money
            i += 1
        print str(int(money))