num = int(input())


for i in list(range(num)):
    print(f'{"*" * (i+1)}'.rjust(num))
    #                      오른쪽 정렬 칸 남기기