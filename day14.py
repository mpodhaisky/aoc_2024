import time
from collections import Counter, defaultdict
import hashlib
import re
from math import prod

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    M,N = 103, 101
    res=Counter()
    for line in data.split("\n"):
        c, r, dc, dr= nums(line)
        for _ in range(100):
            r= (r+dr)%M
            c= (c+dc)%N
        if c==N//2 or r==M//2: continue
        res[(0<=c<N//2,0<=r<M//2)]+=1
    return prod(res.values())



def part2(data):
    M,N = 103, 101
    robots=[]
    for line in data.split("\n"):
        c, r, dc, dr = nums(line)
        robots.append((r,c,dr,dc))
    time=0
    maxcascade=0
    res=0
    for _ in range(10000):
        for i, (r,c,dr,dc) in enumerate(robots):
            robots[i]=((r+dr)%M,(c+dc)%N,dr,dc)
        time+=1
        
        robot_set = set((r,c) for r,c,_,_ in robots)
        cascade=0
        for r,c in robot_set:
            cascade+=(r+1,c-1) in robot_set
        if maxcascade < cascade:
            maxcascade=cascade
            res=time
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