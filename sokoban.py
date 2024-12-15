import os
from pynput import keyboard
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid):
    return "\n".join("".join(row) for row in grid)


def parse_data(data):
    grid = list(map(list,data.split("\n")))
    M,N = len(grid), len(grid[0])
    expanded_grid=[]

    for r in range(M):
        expanded_grid.append([])
        for c in range(N):
            if grid[r][c] in ".#": 
                expanded_grid[-1]+=2*[grid[r][c]]
            if grid[r][c]=="O": 
                expanded_grid[-1]+=["[","]"]
            if grid[r][c]=="@":
                expanded_grid[-1]+=["@","."]
    return expanded_grid

grid = parse_data(open(0).read().rstrip())
current_frame=print_grid(grid)
def move(op):
    global current_frame
    try:
        if op.char in "wasd":
        
            op = op.char
            trans={"w":(-1,0),"s":(1,0),"a":(0,-1),"d":(0,1)}
            value={"[":1,"]":-1}
            sr=sc=0

            M,N = len(grid), len(grid[0])
            for r in range(M):
                for c in range(N):
                    if grid[r][c]=="@":
                        sr=r
                        sc=c
            
            dr, dc = trans[op]
            print(dr,dc)
            q=[(sr,sc)]
            seen={(sr,sc)}
            for r, c in q:
                if grid[r+dr][c+dc]=="#": break
                if grid[r+dr][c+dc] in "[]" and (r+dr,c+dc) not in seen:
                    q.append((r+dr,c+dc))
                    seen.add((r+dr,c+dc))
                    if (dr,dc) in ((1,0),(-1,0)):
                        q.append((r+dr,c+dc+value[grid[r+dr][c+dc]]))
                        seen.add((r+dr,c+dc+value[grid[r+dr][c+dc]]))
            else:
                for r, c in q[::-1]:
                    grid[r+dr][c+dc],grid[r][c] = grid[r][c],grid[r+dr][c+dc]
            current_frame = print_grid(grid)
    except:
        pass

listener = keyboard.Listener(on_press=move)
listener.start()


try:
    while True:
        clear_screen()
        print(current_frame)
        time.sleep(0.1)  # Small delay to reduce CPU usage
except KeyboardInterrupt:
    clear_screen()
    print("Game exited!")
    listener.stop()