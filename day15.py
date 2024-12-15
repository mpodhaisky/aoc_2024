import time
from collections import Counter, defaultdict
import hashlib
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    grid , moves = data.split("\n\n")
    grid=list(map(list,grid.split("\n")))
    M,N = len(grid), len(grid[0])
    trans={"^":(-1,0),"v":(1,0),"<":(0,-1),">":(0,1)}
    sr=sc=0
    for r in range(M):
        for c in range(N):
            if grid[r][c]=="@":
                sr=r
                sc=c
    for op in moves:
        if op == "\n": continue
        dr, dc = trans[op]
        for l in range(1,max(M,N)):
            if not (0<=sr+dr*l<M and 0<=sc+dc*l<N) or grid[sr+dr*l][sc+dc*l]=="#": break
            if grid[sr+dr*l][sc+dc*l]==".":
                grid[sr+dr*l][sc+dc*l], grid[sr+dr][sc+dc]=grid[sr+dr][sc+dc],grid[sr+dr*l][sc+dc*l]
                grid[sr+dr][sc+dc],grid[sr][sc] = grid[sr][sc],grid[sr+dr][sc+dc]
                sr+=dr
                sc+=dc
                break
        
    return sum(100*r+c for r in range(M) for c in range(N) if grid[r][c]=="O")

def part2(data):
    grid , moves = data.split("\n\n")
    grid=list(map(list,grid.split("\n")))
    M,N = len(grid), len(grid[0])
    trans={"^":(-1,0),"v":(1,0),"<":(0,-1),">":(0,1)}
    value={"[":1,"]":-1}
    sr=sc=0

    expanded_grid=[]

    for r in range(M):
        expanded_grid.append([])
        for c in range(N):
            if grid[r][c] in ".#": 
                expanded_grid[-1]+=2*[grid[r][c]]
            if grid[r][c]=="O": 
                expanded_grid[-1]+=["[","]"]
            if grid[r][c]=="@":
                expanded_grid[-1]+=["@","."]
    M,N = len(expanded_grid), len(expanded_grid[0])
    for r in range(M):
        for c in range(N):
            if expanded_grid[r][c]=="@":
                sr=r
                sc=c
                
    for op in moves:
        if op == "\n": continue
        dr, dc = trans[op]
        q=[(sr,sc)]
        seen={(sr,sc)}
        for r, c in q:
            if expanded_grid[r+dr][c+dc]=="#": break
            if expanded_grid[r+dr][c+dc] in "[]" and (r+dr,c+dc) not in seen:
                q.append((r+dr,c+dc))
                seen.add((r+dr,c+dc))
                if (dr,dc) in ((1,0),(-1,0)):
                    q.append((r+dr,c+dc+value[expanded_grid[r+dr][c+dc]]))
                    seen.add((r+dr,c+dc+value[expanded_grid[r+dr][c+dc]]))
        else:
            for r, c in q[::-1]:
                expanded_grid[r+dr][c+dc],expanded_grid[r][c] = expanded_grid[r][c],expanded_grid[r+dr][c+dc]
            sr+=dr
            sc+=dc
    return sum(100*r+c for r in range(M) for c in range(N) if expanded_grid[r][c]=="[")


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