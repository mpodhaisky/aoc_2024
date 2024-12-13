import time
from collections import Counter, defaultdict
import hashlib
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    res=0
    for group in data.split("\n\n"):
        a, b, c = group.split("\n")
        x1, y1 = nums(a)
        x2,y2 = nums(b)
        xt, yt = nums(c)
        
        #A*x1*y2 + (yt-A*y1)*x2 = xt*y2 
        #A*x1*y2  - A*y1*x2 = xt*y2-yt*x2

        A  = (xt*y2-yt*x2)//(x1*y2-y1*x2)
        B = (xt -A*x1)//x2

        if (A*x1+B*x2,A*y1+B*y2) == (xt,yt):
            res+=3*A + B
    return res

def part2(data):
    res=0
    for group in data.split("\n\n"):
        a, b, c = group.split("\n")
        x1, y1 = nums(a)
        x2,y2 = nums(b)
        xt, yt = nums(c)
        xt+=10000000000000
        yt+=10000000000000
        
        #A*x1*y2 + (yt-A*y1)*x2 = xt*y2 
        #A*x1*y2  - A*y1*x2 = xt*y2-yt*x2

        A  = (xt*y2-yt*x2)//(x1*y2-y1*x2)
        B = (xt -A*x1)//x2

        if (A*x1+B*x2,A*y1+B*y2) == (xt,yt):
            res+=3*A + B
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