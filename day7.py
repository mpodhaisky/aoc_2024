import time
from collections import Counter
import hashlib
import re
from collections import defaultdict
from functools import cache
# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))


def part1(data):
    out=0
    for line in data.split("\n"):
        N = nums(line)
        target = N[0]
        def dfs(i,s):
            if i==len(N) and s==target: return True
            if i>=len(N): return False
            return dfs(i+1,N[i]*s) | dfs(i+1,N[i]+s)
        if dfs(1,0):
            out+=target
    return out
        
def part2(data):
    out=0
    for line in data.split("\n"):
        N = nums(line)
        target = N[0]
        def dfs(i,s):
            if i==len(N) and s==target: return True
            if i>=len(N): return False
            return dfs(i+1,N[i]*s) | dfs(i+1,N[i]+s) | dfs(i+1,int(str(s)+str(N[i])))
        if dfs(1,0):
            out+=target
    return out


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