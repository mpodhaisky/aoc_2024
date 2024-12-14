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
        r= (r+100*dr)%M
        c= (c+100*dc)%N
        if c==N//2 or r==M//2: continue
        res[(0<=c<N//2,0<=r<M//2)]+=1
    return prod(res.values())



def part2(data):
    M,N = 103, 101
    robot_count = len(data.split("\n"))
    for time in range(M*N):
        seen=set()
        for line in data.split("\n"):
            c, r, dc, dr= nums(line)
            r= (r+time*dr)%M
            c= (c+time*dc)%N
            seen.add((r,c))
        if len(seen)==robot_count:
            return time


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