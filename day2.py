from aocd import get_data
import time
from collections import Counter

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}

def is_valid_line(differences):
    return (all(n>0 for n in differences) or all(n<0 for n in differences)) and all(abs(n) in range(1,4) for n in differences)

def part1(data):
    res=0
    for line in data.split("\n"):
        line =list(map(int,line.split()))
        deltas = [b-a for a,b in zip(line, line[1:])]
        res+= is_valid_line(deltas)
    return res

def part2(data):
    res=0
    for line in data.split("\n"):
        line = list(map(int,line.split()))
        for i in range(len(line)+1): # add plus one here to make sure valid lines stay valid
            chunked = line[:i]+line[i+1:]
            deltas = [b-a for a,b in zip(chunked, chunked[1:])]
            if is_valid_line(deltas):
                res+=1
                break
    return res


if __name__ == "__main__":
    day, year = 2, 2024
    data = get_data(day=day, year=year)
    t1 = time.time()
    res1 = part1(data)
    t2 = time.time()
    res2 = part2(data)
    t3 = time.time()
    print(f"----------------day {str(day).zfill(2)}-----------------")
    print("----------------Part 1-----------------")
    print(f"time: {t2-t1}")
    print(f"flag: {res1}")
    print("----------------Part 2-----------------")
    print(f"time: {t3-t2}")
    print(f"flag: {res2}")