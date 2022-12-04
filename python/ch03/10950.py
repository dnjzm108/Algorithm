total = int(input())

for i in list(range(total)):
    a,b = input().split()
    a,b = int(a),int(b)
    print(f'{a+b}')