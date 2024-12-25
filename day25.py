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

def part1(data):
    locks,pins = set(), set()
    for grid in data.split("\n\n"):
        grid=grid.split("\n")
        grid=list(map(list,zip(*grid)))
        if grid[0][0]==".":
            pins.add(tuple(row.count("#")-1 for row in grid))
        else:
            locks.add(tuple(row.count("#")-1 for row in grid))

        
    print(locks,pins)
    total=0
    for l in locks:
        for p in pins:
            total+=all(a+b<6 for a, b in zip(l,p))
    return total


if __name__ == "__main__":
    data = open(0).read().rstrip()
    t1 = time.time()
    res1 = part1(data)
    t2 = time.time()
    print("----------------Part 1-----------------")
    print(f"time: {(t2-t1)*1000}".split(".")[0] + " ms")
    print(f"flag: {res1}")