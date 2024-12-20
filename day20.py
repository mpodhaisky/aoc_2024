import time
from collections import Counter, defaultdict,deque
import hashlib
import re
import math
import heapq

adj4 = [(-1,0),(0,1),(1,0),(0,-1)]
adj8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    grid = data.split("\n")
    M,N = len(grid), len(grid[0])
    sr=sy=None
    tr=ty=None
    for r in range(M):
        for c in range(N):
            if grid[r][c]=="S":
                sr,sy=r,c
            if grid[r][c]=="E":
                tr,ty=r,c
    q=[(0,sr,sy)]
    seen={(sr,sy):0}
    for step,r, c in q:
        if (r,c)==(tr,ty):
            break
        for dr, dc in adj4:
            if 0<=r+dr<M and 0<=c+dc<N and (r+dr,c+dc) not in seen and grid[r+dr][c+dc]!="#":
                q.append((step+1,r+dr,c+dc))
                seen[(r+dr,c+dc)]=step+1
    cheats=set()
    for r, c in seen:
        for dr, dc in adj4:
            for ddr, ddc in adj4:
                nr = r+ dr +ddr
                nc = c+ dc +ddc
                if abs(r-nr)+abs(c-nc) == 2 and (nr,nc) in seen and seen[(nr,nc)]-seen[(r,c)]-2 >=100:
                    cheats.add((r,c,nr,nc))
    return len(cheats)
    




def part2(data):
    grid = data.split("\n")
    M,N = len(grid), len(grid[0])
    sr=sy=None
    tr=ty=None
    for r in range(M):
        for c in range(N):
            if grid[r][c]=="S":
                sr,sy=r,c
            if grid[r][c]=="E":
                tr,ty=r,c
    q=[(0,sr,sy)]
    seen={(sr,sy):0}
    for step,r, c in q:
        if (r,c)==(tr,ty):
            break
        for dr, dc in adj4:
            if 0<=r+dr<M and 0<=c+dc<N and (r+dr,c+dc) not in seen and grid[r+dr][c+dc]!="#":
                q.append((step+1,r+dr,c+dc))
                seen[(r+dr,c+dc)]=step+1
    cheats=set()
    for r, c in seen:
        for dr, dc in seen:
            if abs(r-dr)+abs(c-dc) <= 20 and seen[(dr,dc)]-seen[(r,c)]-(abs(r-dr)+abs(c-dc)) >=100:
                cheats.add((r,c,dr,dc))
            
    return len(cheats)


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