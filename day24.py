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
    wires , rules = data.split("\n\n")
    adj = {}
    name={}
    value=Counter()
    for conn in wires.split("\n"):
        a, b = conn.split(": ")
        value[a] = int(b)
    for line in rules.split("\n"):
        a, b = line.split(" -> ")
        fr, op, to = a.split()
        fr, to = sorted((fr,to))
        adj[b] = (op,fr, to)
        name[(op,fr, to)]=b
        name[(op,to,fr)]=b
    
   
    real_adj={"z00":("XOR", "x00","y00"),"c0":("AND", "x00","y00")}

    for i in range(1,46):
        xxory = ("XOR","x"+str(i).zfill(2),"y"+str(i).zfill(2))
        real_adj["xor"+str(i)]=xxory
        xandy =("AND","x"+str(i).zfill(2),"y"+str(i).zfill(2))
        real_adj["and"+str(i)]=xandy
        real_adj["z"+str(i).zfill(2)]=("XOR","xor"+str(i),"c"+str(i-1))
        left_term = ("AND","c"+str(i-1),"xor"+str(i))
        real_adj["leftterm"+str(i)]=left_term
        real_adj["c"+str(i)]=("OR","leftterm"+str(i),"and"+str(i))



    def dfs(n,m):
        if n in value or m in value:return n==m
        op1,l1, r1 = real_adj[n]
        op2,l2,r2 = adj[m]
        return op1==op2 and ((dfs(l1,l2) and dfs(r1,r2)) or(dfs(l1,r2) and dfs(r1,l2)))
    

    res=[]

    for n in ("z"+str(i).zfill(2) for i in range(45)):
        if not dfs(n,n):
            for b in adj:
                for c in adj:
                    adj[b],adj[c]=adj[c],adj[b]
                    if dfs(n,n):
                        res.extend([b,c])
                        break
                    adj[b],adj[c]=adj[c],adj[b]
                else:
                    continue
                break
    return ",".join(sorted(res))


    


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


