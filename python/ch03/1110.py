num = int(input())

_num = num
count = 0

while True:
    a = _num // 10
    b = _num % 10
    c = (a+b) % 10

    _num = (b * 10)+c
    count += 1

    if _num == num:
        break

print(count)
