from aocd import get_data
import time
from collections import Counter

# trans={"U":(-1,0),"L":(0,-1), "D":(1,0),"R":(0,1)}


def part1(data):
    c, d= [], []
    for line in data.split("\n"):
        a, b = line.split("   ")
        c.append(int(a))
        d.append(int(b))
    c.sort()
    d.sort()
    return sum(abs(b-a) for a, b in zip(c,d))



def part2(data):
    c, d= [], []
    for line in data.split("\n"):
        print(line)
        a, b = line.split("   ")
        c.append(int(a))
        d.append(int(b))
    d=Counter(d)
    return sum(a*d[a] for a in c)


if __name__ == "__main__":
    day, year = 1, 2024
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