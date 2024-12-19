import time
from collections import Counter, defaultdict
import hashlib
import re
import math
import heapq
from functools import reduce, cache
import ahocorasick

adj4 = [(-1,0),(0,1),(1,0),(0,-1)]
adj8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]



# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}
def nums(line):
    return list(map(int,re.findall(r'-?\d+', line)))

def part1(data):
    a, b = data.split("\n\n")
    res=0
    automaton = ahocorasick.Automaton()
    for word in a.split(", "):
        automaton.add_word(word,(len(word),word))
    automaton.make_automaton()
    for line in b.split("\n"):
        dp = [1]+[0]*len(line)
        for hi , (_,word) in automaton.iter(line):
            lo = hi - len(word)+1
            dp[hi+1]|=dp[lo]
        res+=dp[-1]
    return res


def part2(data):
    a, b = data.split("\n\n")
    res=0
    automaton = ahocorasick.Automaton()
    for word in a.split(", "):
        automaton.add_word(word,(len(word),word))
    automaton.make_automaton()
    for line in b.split("\n"):
        dp = [1]+[0]*len(line)
        for hi , (_,word) in automaton.iter(line):
            lo = hi - len(word)+1
            dp[hi+1]+=dp[lo]
        res+=dp[-1]
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