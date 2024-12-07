import time
from collections import Counter
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern, data)
    res=0
    for match in matches:
        a,b = nums(match)
        res+=a*b
    return res

def part2(data):
    flag=True 
    pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
    matches = re.findall(pattern, data)
    res=0
    for match in matches:
        if match =="do()": flag=True
        elif match=="don't()": flag=False
        elif flag:
            a, b = nums(match)
            res+=a*b
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