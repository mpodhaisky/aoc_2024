import time
from collections import Counter
import hashlib
import re

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    search_word="XMAS"
    grid=data.split("\n")
    res=0
    M,N = len(grid), len(grid[0])
    for r in range(M):
        for c in range(N):
            for dr, dc in ((-1,-1),(1,1),(1,-1),(-1,1),(1,0),(-1,0),(0,-1),(0,1)):
                for i in range(len(search_word)):
                    if not 0<=r+dr*i<M or not 0<=c+dc*i<N or not grid[r+dr*i][c+dc*i]==search_word[i]: break
                else:
                    res+=1
    return res



def part2(data):
    search_word="MAS"
    grid=data.split("\n")
    res=Counter()
    M,N = len(grid), len(grid[0])
    for r in range(M):
        for c in range(N):
            for dr, dc in ((-1,-1),(1,1),(1,-1),(-1,1)):
                for i in range(len(search_word)):
                    if not 0<=r+dr*i<M or not 0<=c+dc*i<N or not grid[r+dr*i][c+dc*i]==search_word[i]: break
                else:
                    res[(r+dr,c+dc)]+=1
    return sum(n==2 for n in res.values())


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