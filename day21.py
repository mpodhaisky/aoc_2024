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
    grid1=["789","456","123","B0A"]
    grid2=["B^A","<v>"]
    trans={(-1,0):"^",(1,0):"v",(0,1):">",(0,-1):"<"}
    def bfs(start, end,grid):
        if start == end: return [""]
        M,N = len(grid), len(grid[0])
        sr=sc=tr=tc=None
        for r in range(M):
            for c in range(N):
                if grid[r][c]==start:
                    sr,sc = r,c
                if grid[r][c]==end:
                    tr,tc=r,c
        q=[("",sr,sc)]
        res=[]
        for word, r, c in q:
            if (r,c)==(tr,tc):
                break
            for dr, dc in adj4:
                if 0<=r+dr<M and 0<=c+dc<N and grid[r+dr][c+dc]!="B":
                    q.append((word+trans[(dr,dc)],r+dr,c+dc))
                if (r+dr,c+dc)==(tr,tc):
                    res.append(word+trans[(dr,dc)])
        return res

    @cache
    def dfs(start,end):
        return bfs(start,end,grid2)

    total=0
    for line in data.split("\n"):
        chunks=[bfs(start,end,grid1) for start, end in zip("A"+line,line)]
        alignments=[]
        for l in chunks[0]:
            for m in chunks[1]:
                for n in chunks[2]:
                    for k in chunks[3]:
                        alignments.append(l+"A"+m+"A"+n+"A"+k+"A")
        
        miniminsofar=float("inf")
        for alignment in alignments:
            foofoo=0
            for start, end in zip("A"+alignment,alignment):
                first_level = [n+"A" for n in dfs(start,end)]
                minsofar=float("inf")
                for alignment in first_level:
                    foo=0
                    for start, end in zip("A"+alignment,alignment):
                        foo+=min(len(n+"A") for n in dfs(start,end))
                    minsofar=min(foo,minsofar)
                foofoo+=minsofar
            miniminsofar=min(miniminsofar,foofoo)
        total+=miniminsofar*int(line[:-1])

    return total
        
        
            
        


def part2(data):
    pass


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