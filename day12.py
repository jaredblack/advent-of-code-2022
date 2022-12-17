import math
import heapq

def in_bounds(i, j, grid):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

in_file = open('in/day12.txt')
st = in_file.read()
in_file.close()

grid = [[ord(x) - 97 for x in line] for line in st.splitlines()]
dist = [[math.inf for n in range(len(grid[0]))] for _ in range(len(grid))]

potential_starts = []
for i, line in enumerate(grid):
    for j, n in enumerate(line):
        if n == -14:
            line[j] = 0
            dist[i][j] = 0
            src = (i,j)
        if n == -28:
            line[j] = 25
            dest = (i,j)
        if line[j] == 0:
            potential_starts.append((i,j))

q = [(dist[i][j], n, (i, j)) for i, line in enumerate(grid) for j, n in enumerate(line)]
heapq.heapify(q)

while len(q):
    u = heapq.heappop(q)
    ui, uj = u[2]
    if dist[ui][uj] != u[0]:
        continue
    for i, j in [(ui - 1, uj), (ui + 1, uj), (ui, uj + 1), (ui, uj - 1)]:
        if in_bounds(i, j, grid) and grid[i][j] <= grid[ui][uj] + 1:
            if dist[i][j] > dist[ui][uj] + 1:
                dist[i][j] = dist[ui][uj] + 1
                heapq.heappush(q, (dist[i][j], u[1], (i,j)))


print(dist[dest[0]][dest[1]])

# Part 2
dist = [[math.inf for n in range(len(grid[0]))] for _ in range(len(grid))]
min_dist = math.inf
for start in potential_starts:
    si, sj = start
    dist[si][sj] = 0
    q = [(dist[i][j], n, (i, j)) for i, line in enumerate(grid) for j, n in enumerate(line)]
    heapq.heapify(q)
    while len(q):
        u = heapq.heappop(q)
        ui, uj = u[2]
        if dist[ui][uj] != u[0]:
            continue
        for i, j in [(ui - 1, uj), (ui + 1, uj), (ui, uj + 1), (ui, uj - 1)]:
            if in_bounds(i, j, grid) and grid[i][j] <= grid[ui][uj] + 1:
                if dist[i][j] > dist[ui][uj] + 1:
                    dist[i][j] = dist[ui][uj] + 1
                    heapq.heappush(q, (dist[i][j], u[1], (i,j)))
    if dist[dest[0]][dest[1]] < min_dist:
        min_dist = dist[dest[0]][dest[1]] 

print(min_dist)