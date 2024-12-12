import time
from collections import Counter
import hashlib
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    pass

def part2(data):
    grid = list(map(list,data.split("\n")))
    M, N = len(grid), len(grid[0])
    seen=set()
    def fill(r,c, character):
        if not 0<=r<M or not 0<=c<N or (r,c) in seen or grid[r][c] != character: return (0,[])
        seen.add((r,c))
        perimeter = []
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            if not (0<=r+dr<M and 0<=c+dc<N) or grid[r+dr][c+dc]!=character:
                perimeter.append((r,c,dr,dc))
        rra,rrb=0,perimeter
        for (a, b) in (fill(r+1,c,character),fill(r,c+1,character),fill(r-1,c,character),fill(r,c-1,character)):
            rra+=a
            rrb+=b
        return (rra+1,rrb)


    res=0
    for r in range(M):
        for c in range(N):
            if (r,c) not in seen:
                area, perimeter = fill(r,c, grid[r][c])
                idx={}
                for i, n in enumerate(perimeter):
                    idx[n]=i
                perimeter=set(perimeter)
                Parent =list(range(len(perimeter)))

                def find(x):
                    if Parent[x]!=x:
                        return find(Parent[x])
                    else: return x
                
                def union(x,y):
                    try:
                        Parent[find(idx[y])]=find(idx[x])
                    except:
                        pass
                visited=set()
                for r, c, _, _ in perimeter:
                    for (a, b) in ((r,c,-1,0),(r,c-1,-1,0)),((r,c,-1,0),(r,c+1,-1,0)),((r,c,1,0),(r,c-1,1,0)),((r,c,1,0),(r,c+1,1,0)),((r,c,0,-1),(r-1,c,0,-1)),((r,c,0,-1),(r+1,c,0,-1)),((r,c,0,1),(r-1,c,0,1)),((r,c,0,1),(r+1,c,0,1)):
                        if (b, a) not in visited:
                            union(a,b)
                            
                sides = len(set(find(n) for n in Parent))
                res+=sides * area
                    
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