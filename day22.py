import time
from collections import Counter, defaultdict
import hashlib
import re
import math
import heapq

adj4 = [(-1,0),(0,1),(1,0),(0,-1)]
adj8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def step(n):
    m=n
    m*=64
    m^=n
    m%=16777216
    n=m
    m//=32
    m^=n
    m%=16777216
    n=m
    m*=2048
    m^=n
    m%=16777216
    return m

def part1(data):
    total=0
    for line in data.split("\n"):
        n=int(line)
        for _ in range(2000):
            n=step(n)
        total+=n
    return total


def part2(data):
    total=Counter()
    for line in data.split("\n"):
        n=int(line)
        q=[n%10]
        seen=set()
        for _ in range(2000):
            n=step(n)
            q.append(n%10)
            if len(q)>=5:
                seq = tuple(b-a for a, b in zip(q[-5:],q[-4:]))
                if seq not in seen:
                    seen.add(seq)
                    total[seq]+=n%10
    return max(total.values())

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