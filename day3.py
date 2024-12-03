import time
from collections import Counter
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}

def part1(data):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, data)
    res=0
    for a,b in matches:
        res+=int(a)*int(b)
    return res

def part2(data):
    modified=[]
    flag=True 
    for i in range(len(data)):
        if data[i:].startswith("do()"): flag=True
        if data[i:].startswith("don't()"):flag=False
        if flag: modified.append(data[i])
    data="".join(modified)
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, data)
    res=0
    for a,b in matches:
        res+=int(a)*int(b)
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