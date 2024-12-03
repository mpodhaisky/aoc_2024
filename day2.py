import time
from collections import Counter
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def is_nondecreasing(nums):
    return all(1<=b-a<=3 for a,b in zip(nums,nums[1:]))

def is_nonincreasing(nums):
    return all(-3<=b-a<=-1 for a,b in zip(nums,nums[1:]))

def part1(data):
    res=0
    for line in data.split("\n"):
        line =nums(line)
        res+= is_nondecreasing(line) or is_nonincreasing(line)
    return res

def part2(data):
    res=0
    for line in data.split("\n"):
        line =nums(line)
        if is_nondecreasing(line) or is_nonincreasing(line):
            res+=1
            continue
        is_valid=False
        for i in range(1,len(line)):
            if line[i]-line[i-1] not in range(1,4):
                is_valid |= is_nondecreasing(line[:i]+line[i+1:]) or is_nondecreasing(line[:(i-1)]+line[i:])
                break
        for i in range(1,len(line)):
            if line[i]-line[i-1] not in range(-3,0):
                is_valid |= is_nonincreasing(line[:i]+line[i+1:]) or is_nonincreasing(line[:(i-1)]+line[i:])
                break
        res+=is_valid
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