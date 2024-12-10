import time
from collections import Counter
import hashlib
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    grid=list(map(list,data.split("\n")))
    M,N=len(grid),len(grid[0])
    starts=[]
    for r in range(M):
        for c in range(N):
            if grid[r][c]=="0":
                starts.append((r,c))
    res=0
    for r, c in starts:
        q=[(r,c)]
        seen=set(q)
        for a, b in q:
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                if 0<=a+dr<M and 0<=b+dc<N and (int(grid[a+dr][b+dc])-int(grid[a][b]))==1 and (a+dr,b+dc) not in seen:
                    seen.add((a+dr,b+dc))
                    q.append((a+dr,b+dc))
                    res+=grid[a+dr][b+dc]=="9"
    return res

def part2(data):
    grid=list(map(list,data.split("\n")))
    M,N=len(grid),len(grid[0])
    starts=[]
    for r in range(M):
        for c in range(N):
            if grid[r][c]=="0":
                starts.append((r,c))
    global res
    res=0
    for r, c in starts:
        seen=set()
        def dfs(a,b):
            global res
            if grid[a][b]=="9":
                res+=1
                return
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                if 0<=a+dr<M and 0<=b+dc<N and (int(grid[a+dr][b+dc])-int(grid[a][b]))==1 and (a+dr,b+dc) not in seen:
                    seen.add((a+dr,b+dc))
                    dfs(a+dr,b+dc)
                    seen.remove((a+dr,b+dc))
        dfs(r,c)
    return res


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