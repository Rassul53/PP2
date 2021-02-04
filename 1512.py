a = input().split(',')
cnt = 0

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j] and i < j: cnt += 1
print(cnt)