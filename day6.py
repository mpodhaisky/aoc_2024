import time
from collections import Counter
import hashlib
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    grid = data.split("\n")
    M,N=len(grid),len(grid[0])
    sr, sc = 0, 0
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col=="^":
                sr, sc = r, c
                break
    q=[(sr,sc,-1,0)]
    seen=set()
    for a, b, dr, dc in q:
        if (a,b,dr,dc) in seen: return 0
        seen.add((a,b,dr,dc))
        if 0<=a+dr<M and 0<=b+dc<N and grid[a+dr][b+dc]!="#":
            q.append((a+dr,b+dc,dr,dc))
        elif 0<=a+dr<M and 0<=b+dc<N:
            dr, dc = dc, -dr
            q.append((a,b,dr,dc))
    return len(set((a,b) for a,b,_,_ in seen))
        


def part2(data):
    grid=list(map(list,data.split("\n")))
    res=0
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col==".":
                grid[r][c]="#"
                res+=not part1("\n".join("".join(row) for row in grid))
                grid[r][c]="."
    return res


if __name__ == "__main__":
    data = open(0).read().rstrip()
    t1 = time.time()
    res1 = part1(data)
    t2 = time.time()
    res2 = part2(data)
    t3 = time.time()
    print("----------------Part 1-----------------")
    print(f"time: {t2-t1}")
    print(f"flag: {res1}")
    print("----------------Part 2-----------------")
    print(f"time: {t3-t2}")
    print(f"flag: {res2}")