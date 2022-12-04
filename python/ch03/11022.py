import sys

num = int(input())

for i in list(range(num)):
    a,b = map(int,sys.stdin.readline().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')