from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))   

def bfs(x,y):
    visited[x][y] = True
    queue = deque([(x,y)])

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True


visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            cnt += 1
            bfs(i,j)

print(cnt)
