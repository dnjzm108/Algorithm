# #  입력 값에 제곱 값 보여주기
# test = int(input());
# print(test * test)


# # while 문
# num = 1
# while num < 10:
#     print(num)
#     num += 1


# # 입력 값 만큼 반복하여 보여주기
# test = int(input())
# num = 0
# while num < test:
#     print('',test)
#     num += 1


# # 제곱근 표
# input = int(input())
# num = 1
# while num <= input:
#     print(num,num * num)
#     num += 1

# # round() 반올림 해주는 함수 첫번째 인자값 - 반올림 할 수 두번째 인자값 - 소수점 자리수 
# print( round(3.723) )

# height = 100
# bounce = 3/5
# i = 1
# while i <= 10:
#     height = height * bounce
#     print(i,round(height,4))
#     i += 1 

# arr = [60.0,36.0,21.599999999999998,12.959999999999999,7.775999999999999,4.6655999999999995,2.7993599999999996,1.6796159999999998,1.0077695999999998,0.6046617599999998]
# for i in arr:
#     print(round(i,4))


# # 실행 하여 나오는 결과 값은?  853  //는 몫을 구함 853 // 10 은 85
# number = 358

# rem = rev = 0
# while number >= 1:
#     rem = number % 10
#     rev = rev * 10 + rem
#     number = number // 10
# print(rev)

# # if - elif - else 문
# a = 1234 * 4
# b = 13456 / 2

# if a > b:
#     print('a')
# else:
#     print('b')

# c = 15 * 5
# d = 15 + 15 + 15 + 15 + 15
# if c > d:
#     print('c is greater than d')
# elif c == d:
#     print('c is equal to d')
# elif c < d:
#     print('c is less than d')
# else:
#     print('I don\'t know')

# a = 48
# b = 4
# if a % b == 0:
#     print(f'{a}는 {b}로 나우어 떨어집니다.')
# elif a % b != 0:
#     print(f'{a}는 {b}로 나우어 떨어지지 않습니다.')


# # 조건에 따라 반복문 중단하기
# max = 10

# while True:
#     num = int(input())
#     if num > max:
#         print(num,'is too big!')
#         break


# # 숫자 읽기 (입력된 1~3 을 한글로 표시)
# input = int(input())
#
# if input == 1:
#     print('일')
# elif input == 2:
#     print('이')
# elif input == 3:
#     print('삼')


# # 단위 기호 
# num = int(input())
# result = str(num)

# if num >= 1000000000000000000:
#     result = str(num // 1000000000000000000) + 'E'
# elif num >= 1000000000000000:
#     result = str(num // 1000000000000000) + 'P'
# elif num >= 1000000000000:
#     result = str(num // 1000000000000) + 'T'
# elif num >= 1000000000:
#     result = str(num // 1000000000) + 'G'
# elif num >= 1000000:
#     result = str(num // 1000000) + 'M'
# elif num >= 1000:
#     result = str(num // 1000) + 'k'
# elif num >= 0:
#     pass

# print(result)


# # 양수만 덧셈하고 음수일 경우 정지
# sum = 0

# while True:
#     num = int(input())
#     if num < 0:
#         break
#     else:
#         sum += num
# print(sum)


# # 윤년 판별하기 
# num = int(input())
# result = False

# if num % 4 == 0:
#     if num % 100 == 0:
#         if num % 400 ==0:
#             result = True
#         else:
#             result = False
#     else:
#         result = True
# else:
#    result = False

# if result:
#     print(f'{num} 년도는 윤년입니다.')
# else:
#     print(f'{num} 년도는 평년 입니다.')


# # if 문에 and/or 사용하기 
# s = 'banana'

# if 'a' in s:
#     if 'b' in 'banana':
#         print('banana에는 a도 있고 b도 있어요!')

# a = 3
# b = 0
# print( (a*b) > 0 and (a/b) > 0 )

# # for문을 사용하는 반복문  len() - 문자열 길이를 return 하는 함수 

# family = ['mother','father','gentleman','sexy lady']

# for x in family:
#     print(x,len(x))


# # range() 범위를 뜻하는 함수
# # list(range(2,7)) - 파이썬3  range(2,7) - 파이썬2  2이상 7미만인 숫자 리스트 [2,3,4,5,6]
# test = list(range(2,7))
# print(test)

# # range() 로 for문 사용 [4,5,6,7]
# for i in range(4,8):
#     print(i)


# # for문 으로 입력 받은 숫자만큼 반복 하기

# num = int(input())

# for i in range(num):
#     print('',num)


# # for문 으로 제곱근표
# num = int(input())
# for i in range(1,num+1):
#     print(i,i*i)

# #  화학실 실험 첫 입력에 최소온도 최대온도 값을 설정 10 20  다음 입력값으로 15분 마다 온도를 측정하여 적정온도를 벗어날 경우 Alert 출력
# #  적정 온도일 경우 Nothing to report 출력  -999 정지
# L = input().split()
# min = int(L[0])
# max = int(L[1])
# # min,max = map(int,input().split())

# temp = int(input())

# while temp != -999:
#     if min <= temp <= max:
#         print('Nothing to report')
#         temp = int(input())
#     else:
#         print('Alert!')
#         break

# # match - case 문 
# for n in range(1,11):
#     match n % 2:
#         case 0:
#             print(f'{n} is even.')
#         case 1:
#             print(f'{n} is odd')

# # FizzBuzz 문제 3으로 나눠지는 수를 Fizz 5로 나눠지는 수를 Buzz 3과5 로 나눠지는 수를 FizzBuzz
# for n in range(1,101):
#     match(n%3,n%5):
#         case (0,0):
#             print('FizzBuzz')
#         case (0,_):
#             print('Fizz')
#         case (_,0):
#             print('Buzz')
#         case (_):
#             print(n)



# # 함수

# def test():
#     for i in range(2,10):
#         for v in range(1,10):
#             print(f'{i} * {v} = {i*v:2d}')
#         print()

# test()

# def multi(m):
#     for n in range(1, 10):
#         print(f'{m} * {n} = {m*n:2d}')

# if __name__ == '__main__':
#     for i in range(2, 10):
#         multi(i)
#         print()


# # 한국 나이 찾는 함수
# from datetime import datetime
# today = datetime.today().year

# def korean_age(age):
#     year = today.year
#     return year - age + 1

# print( korean_age(1995) )


# # 이자 (단리) 계산

# def simple_interest(p,r,t):
#     return p * r * t

# print( simple_interest(10000000, 0.03875, 5) )

# def simple_interest_amount(p,r,t):
#     # return p*(1+r*t)
#     return p + (p * r * t)

# print( simple_interest_amount(10000000, 0.03875, 5) )


# # 이자 (복리) 계산
# # p = 원금 , r = 이율 , t = 기간 , n = 복리 횟수
# def compound_interest_amount(p,r,t,n):
#     return p * (1 + r /n) ** (n * t)

# print( compound_interest_amount(1000000,0.043,3,1) )

# (lambda x,y: print(x + y) )(10,20)

# print( list(map(lambda x : x ** 2 , range(5))) )


# from functools import reduce
# test = reduce(lambda x,y : x + y,range(5))
# print(test)

# test = list( filter( lambda x : x > 5, range(10)) )
# print(test)

# def read(text):
#     ridename, limit = map(str.strip, text.split(':'))

#     cmmin = cmmax = None
#     if '~' in limit:
#         cmmin, cmmax = map(lambda x: int(x.replace('cm', '')), limit.split('~'))
#     elif "이상" in limit:
#         cmmin = int(limit.split("cm")[0])

#     return ridename, cmmin, cmmax


# # 놀이공원  - 키제한 문자열 자르기 
# def read(text):
#    ridename,limit = text.split(':')

#    max = min = None
#    if '~' in limit:
#     max,min = map( lambda x : int(x.replace('cm','')),limit.split('~') )
#     print(max,min)
#    elif '이상' in limit:
#     max = int( limit.split("cm")[0] ) 
    
#    return ridename,min,max

# if __name__ == "__main__":
#     ridename, min, max = read(input())

#     print("이름:", ridename )
#     print("하한:", min)
#     print("상한:", max)


# def test(text):
#     de = text[::-1]
#     if text == de:
#         return True
#     else:
#         return False

# print( test('Anna') )

# def test(text):
#     text = text.lower()
#     de = text[::-1]
#     if text == de:
#         return True
#     else:
#         return False
# print( test('Annaa') )

# def test(text):
#     text = text.lower().replace(' ','')
#     de = text[::-1]
#     if text == de:
#         return True
#     else:
#         return False


# print( test('My gym') )


# def palindrome(s):
#     s = s.lower()
#     s = s.replace(' ', '')
#     return s[:] == s[::-1]

# if __name__ == '__main__':
#     for x in ['anna', 'banana', 'Anna', 'My gym']:
#         if palindrome(x):
#             print(f"'{x}' is a panlindrome")
#         else:
#             print(f"'{x}' is not a palindrome")
