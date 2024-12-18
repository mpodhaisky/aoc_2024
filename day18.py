import time
from collections import Counter, defaultdict
import hashlib
import re

adj4 = [(-1,0),(0,1),(1,0),(0,-1)]
# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    M = 71
    blocked=set()
    cnt=0
    for line in data.split("\n"):
        if cnt >= 1024: break
        blocked.add(tuple(nums(line)))
        cnt+=1
    
    q=[(0,0,0)]
    seen={(0,0)}
    for steps,a, b in q:
        if (a,b) == (M-1,M-1): return steps
        for dr, dc in adj4:
            if 0<=a+dr<M and 0<=b+dc<M and (a+dr,b+dc) not in seen and (a+dr,b+dc) not in blocked:
                seen.add((a+dr,b+dc))
                q.append((steps+1,a+dr,b+dc))
    return -1



def part2(data):
    M = 71
    blocked=[tuple(nums(line)) for line in data.split("\n")]
    blocked_set=set(blocked)
    seen={(0,0)}
    def fill(r,c):
        for dr, dc in adj4:
            if (r+dr,c+dc) not in seen and (r+dr,c+dc) not in blocked_set and (0<=r+dr<M and 0<=c+dc<M):
                seen.add((r+dr,c+dc))
                fill(r+dr,c+dc)
    fill(0,0)
    while blocked:
        r,c = blocked.pop()
        blocked_set.remove((r,c))
        for dr, dc in adj4:
            if (r+dr,c+dc) in seen:
                seen.add((r,c))
                fill(r,c)
                break
        if (M-1,M-1) in seen:
            return f"{r},{c}"

    


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