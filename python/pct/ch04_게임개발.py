n, m = map(int, input().split())
a, b, d = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

cnt = 0
res = 1 # 시작좌표

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
    nd = d-1
    if nd < 0:
        nd = 3
    
    nx = a + dx[nd]
    ny = b + dy[nd]

    if maps[nx][ny] == 1 or maps[nx][ny] == -1:
        cnt += 1
    else:
        maps[nx][ny] = -1
        d = nd
        a = nx
        b = ny
        cnt = 0
        res += 1
        continue

    if cnt == 4:
        bd = nd - 2
        if bd < 0:
            bd += 4
        
        bx = a + dx[bd]
        by = b + dy[bd]

        if maps[bx][by] == 1:
            break

        a = bx
        b = by
        res += 1

print(res)    

# 0 > 3 
# 1 > 0
# 2 > 1
# 3 > 2