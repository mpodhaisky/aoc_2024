import time
from collections import Counter, defaultdict, deque
from heapq import heapify, heappush, heappop
import hashlib
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    ops=[] 
    gaps=deque()
    margin=0
    for i,c in enumerate(data):
        if i%2==0: 
            ops.append((i//2,margin,int(c)))
        else:
            gaps.append((margin,int(c)))
        margin+=int(c)
    res=0
    while ops:
        id, offset, length = ops.pop()
        if gaps[0][0]>=offset:
            res+=sum(range(offset,offset+length))*id
        else:
            gap_index, gap_length = gaps.popleft()
            res+=sum(range(gap_index,gap_index+min(gap_length,length)))*id
            if gap_length > length:
                gaps.appendleft((gap_index+length,gap_length-length))
            elif length>gap_length:
                ops.append((id,offset,length-gap_length))
    return res

def part2(data):
    ops=[] 
    gaps=defaultdict(list)
    margin=0
    for i,c in enumerate(data):
        if i%2==0: 
            ops.append((i//2,margin,int(c)))
        else:
            gaps[int(c)].append(margin)
        margin+=int(c)
    res=0
    for id, offset, length in ops[::-1]:
        gap_offset=gap_length=float("inf")
        for dl in range(length,10):
            while gaps[dl] and gaps[dl][0]>=offset: heappop(gaps[dl])
            if gaps[dl] and gaps[dl][0]<gap_offset:gap_offset, gap_length = gaps[dl][0], dl
        if gap_offset!=float("inf"):
            heappop(gaps[gap_length])
            heappush(gaps[gap_length-length],gap_offset+length)
            res+=sum(range(gap_offset,gap_offset+length))*id
        else:
            res+=sum(range(offset,offset+length))*id
    return res

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