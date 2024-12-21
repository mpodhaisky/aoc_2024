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
        total=0
        grid1 = tuple(map(tuple,[["7","8","9"],["4","5","6"],["1","2","3"],["b","0","A"]]))
        grid2= tuple(map(tuple,[["b","^","A"],["<","v",">"]]))

        @cache
        def seq(start, end,grid):
            if start==end: return [[["A","A"]]]
            N,M = len(grid[0]),len(grid)
            sr=sc=tr=tc=None
            for r in range(M):
                for c in range(N):
                    if grid[r][c]==start:
                        sr, sc = r,c
                    if grid[r][c]==end:
                        tr,tc = r,c
            q=[("",sr,sc)]
            seen=set(q)
            ret=[]
            for word, r, c in q:
                if (tr,tc)==(r,c):
                    break
                for dr, dc in adj4:
                    if (tr,tc) == (r+dr,c+dc):
                        ret.append(word+trans[(dr,dc)])
                    if 0<=r+dr<M and 0<=c+dc<N and grid[r+dr][c+dc]!="b" and (word+trans[(dr,dc)],r+dr,c+dc) not in seen:
                        seen.add((word+trans[(dr,dc)],r+dr,c+dc))
                        q.append((word+trans[(dr,dc)],r+dr,c+dc))
            ret=[list(map(list,zip("A"+row,row))) for row in ret]
            m = min(map(len,ret))
            return [a for a in ret if len(a)==m]

        @cache
        def dfs(depth, start, end):
            if depth ==0: return 0
            res=float("inf")
            for child in seq(start,end,grid2):
                cur = 0
                for a, b in child:
                    cur+=1+dfs(depth-1,a,b)
                res=min(res,cur)
            return res

        for line in data.split("\n"):
            pairs = list(zip("A"+line,line))
            possible_results = [seq(a,b,grid1) for a, b in pairs]
            length=float("inf")
            for a in possible_results[0]:
                for b in possible_results[1]:
                    for c in possible_results[2]:
                        for d in possible_results[3]:
                            b[0][0]=a[-1][1]
                            c[0][0]=b[-1][1]
                            d[0][0]=c[-1][1]
                            print(a+b+c+d)
                            pairs = a+b+c+d
                            length=min(length,sum(dfs(2,*pair) for pair in pairs))
            
            total+= length*int(line[:-1])
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