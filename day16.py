import time
from collections import Counter, defaultdict
import hashlib
import re
import heapq
# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    grid = list(map(list,data.split("\n")))
    M,N = len(grid), len(grid[0])
    sr=sc=tr=tc=None
    for r in range(M):
        for c in range(N):
            if grid[r][c]=="S":
                sr,sc=r,c
            if grid[r][c]=="E":
                tr,tc=r,c
    q=[(0,sr,sc,0,1)]
    seen={(sr,sc,0,1):0}
    while q:
        cost, r, c, dr, dc = heapq.heappop(q)
        if seen[(r,c, dr, dc)] != cost: continue
        if grid[r+dr][c+dc]!="#" and seen.get((r+dr,c+dc,dr,dc),float("inf"))>cost+1:
            seen[(r+dr,c+dc,dr,dc)] =cost+1
            heapq.heappush(q,(cost+1,r+dr,c+dc,dr,dc))
        
        for ddr, ddc in ((dc, -dr), (-dc,dr)):
            if seen.get((r,c,ddr,ddc),float("inf"))> cost +1000:
                seen[(r,c,ddr,ddc)]=cost+1000
                heapq.heappush(q,(cost+1000,r,c,ddr,ddc))
    return min(seen.get((tr,tc,dr,dc),float("inf")) for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)))


def part2(data):
    grid = list(map(list,data.split("\n")))
    M,N = len(grid), len(grid[0])
    sr=sc=tr=tc=None
    for r in range(M):
        for c in range(N):
            if grid[r][c]=="S":
                sr,sc=r,c
            if grid[r][c]=="E":
                tr,tc=r,c
    q=[(0,sr,sc,0,1)]
    seen={(sr,sc,0,1):0}
    parent=defaultdict(list)
    while q:
        cost, r, c, dr, dc = heapq.heappop(q)
        if seen[(r,c, dr, dc)] != cost: continue
        if grid[r+dr][c+dc]!="#" and seen.get((r+dr,c+dc,dr,dc),float("inf"))>=cost+1:
            if seen.get((r+dr,c+dc,dr,dc),float("inf"))>cost+1:
                parent[(r+dr,c+dc,dr,dc)]=[(r,c,dr,dc)]
            else:
                parent[(r+dr,c+dc,dr,dc)].append((r,c,dr,dc))
                continue
            seen[(r+dr,c+dc,dr,dc)] =cost+1
            heapq.heappush(q,(cost+1,r+dr,c+dc,dr,dc))
        
        for ddr, ddc in ((dc, -dr), (-dc,dr)):
            if seen.get((r,c,ddr,ddc),float("inf")) >= cost +1000:
                if seen.get((r,c,ddr,ddc),float("inf")) > cost+1000:
                    parent[(r,c,ddr,ddc)]=[(r,c,dr,dc)]
                else:
                    parent[(r,c,ddr,ddc)].append((r,c,dr,dc))
                    continue
                seen[(r,c,ddr,ddc)]=cost+1000
                heapq.heappush(q,(cost+1000,r,c,ddr,ddc))
    
    q=[(tr,tc,dr,dc) for dr, dc in ((1,0),(-1,0),(0,-1),(0,1))]
    m=min(q,key=lambda x: seen.get(x,float("inf")))
    q= [node for node in q if seen.get(node,float("inf")==m)]
    seen=set(q)
    for node in q:
        for p in parent[node]:
            if p not in seen:
                seen.add(p)
                q.append(p)
    return len({(a,b) for a, b, _,_ in q})
    

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