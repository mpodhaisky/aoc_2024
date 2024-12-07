import time
from collections import Counter
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}

def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    c, d= [], []
    for line in data.split("\n"):
        a, b = nums(line)
        c.append(a)
        d.append(b)
    c.sort()
    d.sort()
    return sum(abs(b-a) for a, b in zip(c,d))



def part2(data):
    c, d= [], Counter()
    for line in data.split("\n"):
        a, b = nums(line)
        c.append(a)
        d[b]+=1
    return sum(a*d[a] for a in c)


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