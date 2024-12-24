import time
from collections import Counter, defaultdict
import hashlib
import re
import math
import heapq
from functools import cache

adj4 = [(-1,0),(0,1),(1,0),(0,-1)]
adj8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    wires , rules = data.split("\n\n")
    adj = {}
    value={}
    for conn in wires.split("\n"):
        a, b = conn.split(": ")
        value[a] = int(b)
    for line in rules.split("\n"):
        a, b = line.split(" -> ")
        fr, op, to = a.split()
        adj[b] = (fr, op, to)
    
    @cache
    def dfs(n):
        if n in value: return value[n]
        l, op, r = adj[n]
        if op =="AND":
            return dfs(l) and dfs(r)
        elif op =="OR":
            return dfs(l) or dfs(r)
        else:
            return dfs(l)!= dfs(r)
    
    res=""
    for n in sorted(list(adj)+list(value)):
        if n[0]=="z":
            res+=str(int(dfs(n)))
    return int(res[::-1],2)



def part2(data):
    pass
                

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





