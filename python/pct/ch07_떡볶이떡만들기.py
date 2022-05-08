n, m = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
end = max(heights)

res = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for h in heights:
        if mid < h:
            total += h - mid
    
    if total >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
