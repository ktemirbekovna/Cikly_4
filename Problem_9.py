a = -100
b = a
x = 0
while a <= 100:
    if a % 13 == 0 and a % 2 == 0:
        print(a, b ** 2)
        x = x + 1
    a += 1
print(x)

x2 = 0
while b <= 100:
    if b % 2 == 1:
        x2 += 1
        print(b)
    b += 7
print(x2)