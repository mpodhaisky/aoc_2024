import time
from collections import Counter
import hashlib
import re
from functools import cache

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

@cache
def dp(n,t):
    if t==0: return 1
    elif n==0: return dp(1,t-1)
    elif len(str(n))%2==0: 
            s=str(n)
            l=len(s)
            return dp(int(s[:l//2]),t-1) + dp(int(s[l//2:]),t-1)
    else: return dp(n*2024,t-1)

def part1(data):
    return sum(dp(n,25) for n in nums(data))
    
    
def part2(data):
    return sum(dp(n,75) for n in nums(data))




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