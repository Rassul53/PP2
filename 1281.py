a = int(input())
p = 1
s = 0
while a != 0:
    d = a % 10
    p *= d
    s += d
    a //= 10
print(p - s)