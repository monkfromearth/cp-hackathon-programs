"""
colors = {(0,0,0):"black", (0,0,1):"blue", (0,1,0):"green", (0,1,1):"cyan", (1,0,0):"red", (1,0,1):"magenta",  (1,1,0):"yellow",  (1,1,1):"white"}
for t in range(int(raw_input().strip())):
    s,r,g,b = map(int, raw_input().strip().split(" "))
    print colors[tuple([((s/i) % 2) for i in [r,g,b]])] 

------------------------------------------------------------
"""

c=["black","blue","green","cyan","red","magenta","yellow","white"]
for t in range(input()):
    s,r,g,b = map(int,raw_input().split())
    print c[int("".join(map(str,[((s/i)%2) for i in [r,g,b]])),2)] 