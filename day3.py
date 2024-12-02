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
    flag=True 
    pattern = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"
    matches = re.findall(pattern, data)
    res=0
    for match in matches:
        a, b, c = match
        if a =="do()": flag=True
        elif a=="don't()": flag=False
        elif flag:
            res+=int(b)*int(c)
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