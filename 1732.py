a = input().split(',')
m = 0
s = 0
for i in a:
    s += int(i)
    m = max(m, s)
print(m)