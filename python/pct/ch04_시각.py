n = int(input())

cnt = 0

# 전체 데이터 수가 100만개 이하면 완전탐색 사용 적절
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1

print(cnt)