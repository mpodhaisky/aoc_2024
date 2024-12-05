import time
from collections import Counter
import hashlib
import re
from collections import defaultdict

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    res=0
    rules , seq = data.split("\n\n")
    adj=defaultdict(list)
    for rule in rules.split("\n"):
        c, d = nums(rule)
        adj[c].append(d)
    
    for line in seq.split("\n"):
        N = nums(line)
        for i in range(len(N)-1,-1,-1):
            for j in range(i):
                if N[j] in adj[N[i]]:
                    break
            else:
                continue
            break
        else:
            res+=N[len(N)//2]
    return res

def part2(data):
    res=0
    rules , seq = data.split("\n\n")
    adj=defaultdict(list)
    for rule in rules.split("\n"):
        c, d = nums(rule)
        adj[c].append(d)
    
    for line in seq.split("\n"):
        N = nums(line)
        for i in range(len(N)-1,-1,-1):
            for j in range(i):
                if N[j] in adj[N[i]]:
                    break
            else:
                continue
            break
        else:
            indeg=defaultdict(int)
            for n in N:
                for child in adj[n]:
                    if child in N:
                        indeg[child]+=1
            q=[n for n in N if indeg[n]==0]
            for n in q:
                for m in adj[n]:
                    indeg[m]-=1
                q+=[m for m in N if indeg[m]==0 and m not in q]
            res+=q[len(q)//2]
    return res


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