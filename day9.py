import time
from collections import Counter
import hashlib
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    res=[]
    for i,c in enumerate(data):
        if i%2==0: res+= [str(i//2) for _ in range(int(c))]
        else: res+=list(int(c)*".")
    
    lo,hi = 0,len(res)-1
    while lo <hi:
        if res[hi]==".": hi-=1
        elif res[lo]!=".": lo+=1
        else: res[hi],res[lo]=res[lo],res[hi]
    
    return sum(i*int(c) for i, c in enumerate(res) if c!=".")
    

def part2(data):
    res=""
    for i,c in enumerate(data):
        if i%2==0: res+= chr((i//2)+100)*int(c)
        else: res+=int(c)*"."
    ops=[]
    margin=0
    for i,c in enumerate(data):
        if i%2==0: 
            ops.append((chr((i//2)+100),margin,int(c)))
        margin+=int(c)
    res=list(res)
    for c, i, l in ops[::-1]:
        for j in range(i-l+1):
            if "".join(res[j:j+l])=="."*l:
                res[j:j+l],res[i:i+l]=res[i:i+l],res[j:j+l]
                break

    return sum(i*(ord(c)-100) for i, c in enumerate(res) if c!=".")

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