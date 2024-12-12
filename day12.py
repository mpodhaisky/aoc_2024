import time
from collections import Counter, defaultdict
import hashlib
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))


def part1(data):
    grid = list(map(list,data.split("\n")))
    M, N = len(grid), len(grid[0])
    
    Parent=list(range(M*N))


    def find(x):
        if Parent[x]!=x:
            return find(Parent[x])
        else: return x
    
    def union(x,y):
        Parent[find(y)]=find(x)
    
    for r in range(M):
        for c in range(N):
            for dr, dc in ((1,0),(0,1),(0,-1),(-1,0)):
                if 0<=r+dr<M and 0<=c+dc<N and grid[r][c]==grid[r+dr][c+dc]:
                    union((r+dr)*N + c+dc,r*N + c)
    tiles=defaultdict(list)
    perimeter=defaultdict(list)
    for i , n in enumerate(find(n) for n in Parent):
        r, c = i//N, i%M
        for dr, dc in ((1,0),(0,1),(0,-1),(-1,0)):
            if not (0<=r+dr<M and 0<=c+dc<N and grid[r][c]==grid[r+dr][c+dc]):
                perimeter[n].append((r,c,dr,dc))
        tiles[n].append((r,c))

    return sum(len(perimeter[n])*len(tiles[n]) for n in tiles)


def part2(data):
    grid = list(map(list,data.split("\n")))
    M, N = len(grid), len(grid[0])
    
    Parent=list(range(M*N))


    def find(x):
        if Parent[x]!=x:
            return find(Parent[x])
        else: return x
    
    def union(x,y):
        Parent[find(y)]=find(x)
    
    for r in range(M):
        for c in range(N):
            for dr, dc in ((1,0),(0,1),(0,-1),(-1,0)):
                if 0<=r+dr<M and 0<=c+dc<N and grid[r][c]==grid[r+dr][c+dc]:
                    union((r+dr)*N + c+dc,r*N + c)
    tiles=defaultdict(list)
    perimeter=defaultdict(list)
    for i , n in enumerate(find(n) for n in Parent):
        r, c = i//N, i%M
        for dr, dc in ((1,0),(0,1),(0,-1),(-1,0)):
            if not (0<=r+dr<M and 0<=c+dc<N and grid[r][c]==grid[r+dr][c+dc]):
                perimeter[n].append((r,c,dr,dc))
        tiles[n].append((r,c))

    sides=defaultdict(list)

    for group, border in perimeter.items():
        idx={}
        Parent=list(range(len(border)))

        def find(x):
            if Parent[x]!=x:
                return find(Parent[x])
            else: return x
        
        def union(x,y):
            Parent[find(y)]=find(x)
        
        for i,n in enumerate(border):
            idx[n]=i
        
        for r, c, dr, dc in border:
            if (r+dc, c-dr, dr, dc) in idx:
                union(idx[(r+dc, c-dr, dr, dc)],idx[(r, c, dr, dc)])
            if (r-dc, c+dr, dr, dc) in idx:
                union(idx[(r-dc, c+dr, dr, dc)],idx[(r, c, dr, dc)])
        sides[group] = list(set(find(n) for n in Parent))

    return sum(len(sides[n])*len(tiles[n]) for n in tiles)


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