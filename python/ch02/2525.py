h, m = input().split()

time = int(input())
h, m = int(h), int(m)

time_h = time // 60
time_m = time % 60

# 60 안넘을 경우
if time < 60:

    # 60분이 넘을 경우
    if m + time_m > 60:
        h += 1
        m = 60 - (m + time_m)
    # 60분 안넘을 경우
    else:
        m += time_m
# 60분 넘을 경우
else:
    h += time_h
    m += time_m

if h >= 24:
    h -= 24

if m >= 60:
    h += 1
    m -= 60

print(h,m)