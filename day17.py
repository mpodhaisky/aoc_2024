import time
from collections import Counter, defaultdict
import hashlib
import re
from functools import cache
from math import log2

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def combo(n,A,B,C):
    if n <=3: return n
    if n==4: return A
    if n==5: return B
    if n==6: return C

def my_program(A,program):
    B=C=0
    for op, input in zip(program[::2],program[1::2]):
        if op in {0,3}: continue
        elif op == 1: B^=input
        elif op==2: B=combo(input,A,B,C)%8
        elif op==4: B^=C
        elif op==5: return combo(input,A,B,C)%8
        elif op==6: B=A>>combo(input,A,B,C)
        elif op==7: C=A>>combo(input,A,B,C)

def part1(data):
    a, b = data.split("\n\n")
    program = list(map(int,b.split(": ")[1].split(",")))
    A=nums(a)[0]
    out=[]
    while A:
        out.append(my_program(A,program))
        A>>=3
    return out


def part2(data):
    _, b = data.split("\n\n")
    program = list(map(int,b.split(": ")[1].split(",")))
    def dfs(cur, i):
        if i>=len(program): return [cur]
        out=[]
        cur <<=3
        for j in range(8):
            if my_program(cur+j,program)==program[-i-1]:
                out+=(dfs(cur+j,i+1))
        return out
    return min(dfs(0,0))

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