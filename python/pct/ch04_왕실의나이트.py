pos = input()

x = ord(pos[0]) - ord('a') + 1
y = int(pos[1])

cnt = 0

cand = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

for cx,cy in cand:
    nx = x + cx
    ny = x + cy

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    cnt += 1

print(cnt)