a = 456
total = 0

while a > 0:
    d = a % 10
    total += d
    a //= 10

print(total)
