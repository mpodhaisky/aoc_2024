import time
from collections import Counter, defaultdict
import hashlib
import re
import math
import heapq
from functools import cache

adj4 = [(-1,0),(0,1),(1,0),(0,-1)]
adj8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
trans = {(-1,0):"^",(0,1):">",(0,-1):"<",(1,0):"v"}

def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))


def part1(data):
    adj = defaultdict(list)
    for line in data.split("\n"):
        fr, to = sorted(line.split("-"))
        adj[fr].append(to)
        adj[to].append(fr)
    
    def is_clique(nodes,new_node):
        for node in nodes:
            if not new_node in adj[node]:
                return False
        return True
    
    res=set()
    for a in adj:
        for b in adj[a]:
            if not is_clique((a,),b):
                continue
            for c in adj[b]:
                if not is_clique((a,b),c) or "t" not in (a[0]+b[0]+c[0]):
                    continue
                res.add(tuple(sorted((a,b,c))))
    return len(res)



        

        
def part2(data):
    adj = defaultdict(list)
    for line in data.split("\n"):
        fr, to = line.split("-")
        adj[fr].append(to)
        adj[to].append(fr)
    
    @cache
    def is_clique(nodes,new_node):
        for node in nodes:
            if not new_node in adj[node]:
                return False
        return True

    max_k = ""
    for n in adj:
        seen={n}
        for m in adj[n]:
            if not is_clique(tuple(sorted(seen)), m):
                continue
            seen.add(m)
        if len(max_k)< len(",".join(sorted(seen))):
            max_k=",".join(sorted(seen))
    return max_k

if __name__ == "__main__":
    data = open(0).read().rstrip()
    t1 = time.time()
    res1 = part1(data)
    t2 = time.time()
    res2 = part2(data)
    t3 = time.time()
    print("----------------Part 1-----------------")
    print(f"time: {(t2-t1)*1000}".split(".")[0] + " ms")
    print(f"flag: {res1}")
    print("----------------Part 2-----------------")
    print(f"time: {(t3-t2)*1000}".split(".")[0] + " ms")
    print(f"flag: {res2}")

