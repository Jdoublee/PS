from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque([(0,0)])

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1:
            queue.append((nx,ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[n-1][m-1])