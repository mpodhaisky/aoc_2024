adj1={}
adj2={}

grid1=("789","456","123","B0A")
grid2=("B^A","<v>")
trans={(-1,0):"^",(1,0):"v",(0,1):">",(0,-1):"<"}
def bfs(start, end,grid):
    if start == end: return ["A"]
    M,N = len(grid), len(grid[0])
    sr=sc=tr=tc=None
    for r in range(M):
        for c in range(N):
            if grid[r][c]==start:
                sr,sc = r,c
            if grid[r][c]==end:
                tr,tc=r,c
    q=[("",sr,sc)]
    res=[]
    for word, r, c in q:
        if (r,c)==(tr,tc):
            break
        for dr, dc in adj4:
            if 0<=r+dr<M and 0<=c+dc<N and grid[r+dr][c+dc]!="B":
                q.append((word+trans[(dr,dc)],r+dr,c+dc))
            if (r+dr,c+dc)==(tr,tc):
                res.append(word+trans[(dr,dc)]+"A")
    return res

for a in "".join(grid1):
    for b in "".join(grid1):
        if "B" not in (a,b):
            adj1[(a,b)]=bfs(a,b,grid1)

for a in "".join(grid2):
    for b in "".join(grid2):
        if "B" not in (a,b):
            adj2[(a,b)]=bfs(a,b,grid2)

print("adj1 = ",adj1)
print("adj2 = ",adj2)