n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

bigNum1 = numbers[-1]
bigNum2 = numbers[-2]

res = 0

while m > 0:
    if n > k:
        res += bigNum1 * k + bigNum2
        m -= (k+1)
    else:
        res += bigNum1 * (k-n)
        m -= k

print(res)