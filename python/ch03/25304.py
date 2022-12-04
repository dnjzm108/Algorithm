total = int(input())
num = int(input())

result = 0

for i in list(range(num)):
    a,b = input().split()
    a,b = int(a),int(b)
    result += a * b

if total == result:
    print('Yes')
else:
    print('No')