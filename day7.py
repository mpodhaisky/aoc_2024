import time
from collections import Counter
import hashlib
import re
from collections import defaultdict
from functools import cache
# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))
def dfs(N,i,s, allow_special_operator):
    if i<0 and not s: return True
    if i<0 or not s: return False
    ret=False
    if allow_special_operator and str(s).endswith(str(N[i])): ret|=dfs(N,i-1,int("0"+str(s)[:len(str(s))-len(str(N[i]))]), allow_special_operator)
    if s%N[i]==0: ret|= dfs(N,i-1,s//N[i], allow_special_operator)
    if s-N[i] >=0: ret|= dfs(N,i-1,s-N[i], allow_special_operator)
    return ret

def part1(data):
    out=0
    for line in data.split("\n"):
        N = nums(line)
        target , arr = N[0], N[1:]
        out+=target*dfs(arr,len(arr)-1,target, False)  
    return out
        
def part2(data):
    out=0
    for line in data.split("\n"):
        N = nums(line)
        target , arr = N[0], N[1:]
        out+=target*dfs(arr,len(arr)-1,target, True)
    return out


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