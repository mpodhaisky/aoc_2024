import time
from collections import Counter, defaultdict, deque
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
    n=((n<<6)^n) % 16777216
    n= ((n << 5)^n) % 16777216
    n= ((n>>11)^n) % 16777216
    return n

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
        cur=Counter()
        q=[int(line)]
        for _ in range(2000): q.append(step(q[-1]))
        for i in range(len(q)-1,3,-1): cur[tuple(q[j]%10-q[j-1]%10 for j in range(i-3,i+1))]=q[i]%10
        total+=cur
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