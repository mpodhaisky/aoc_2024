import time
from collections import Counter, defaultdict
import hashlib
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    grid = list(map(list,data.split("\n")))
    M,N = len(grid), len(grid[0])
    locations=defaultdict(list)

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col!=".":
                locations[col].append((r,c))
    res=set()
    for antenna in locations:
        for i in range(len(locations[antenna])):
            for j in range(i+1,len(locations[antenna])):
                a, b = locations[antenna][i]
                c, d = locations[antenna][j]
                if 0 <= 2*c-a < M and 0<= 2*d-b < N:
                    res.add((2*c-a,2*d-b))
                if 0 <= 2*a-c < M and 0<= 2*b-d < N:
                    res.add((2*a-c,2*b-d))
    return len(res)


def part2(data):
    grid = list(map(list,data.split("\n")))
    M,N = len(grid), len(grid[0])
    locations=defaultdict(list)

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col!=".":
                locations[col].append((r,c))
    res=set()
    for antenna in locations:
        for i in range(len(locations[antenna])):
            for j in range(i+1,len(locations[antenna])):
                a, b = locations[antenna][i]
                c, d = locations[antenna][j]
                for l in range(1000):
                    if 0 <= c+ (c-a)*l < M and 0<= d + (d-b)*l < N:
                        res.add((c+(c-a)*l,d+(d-b)*l))
                    else:
                        break
                for l in range(1000):
                    if 0 <= a+ (a-c)*l < M and 0<= b + (b-d)*l < N:
                        res.add((a+(a-c)*l,b+(b-d)*l))
                    else:
                        break
    return len(res)


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