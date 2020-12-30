# 묵봇 복습장

# Day 1

a = 1   # assign (할당, 왼쪽<-오른쪽)
a = 1 + 2

print(a)

# 파이썬에서는 들여쓰기가 중요

if 4 in [1, 2, 3, 4] : print('I have 4')

languages = ['python', 'perl', 'c', 'java']

for lang in languages :
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%s need complier" % lang)
    else :
        print("should not reach here")

if a==4 :
    print('4')
    print('four')
print("코드블록 밖")

print(5/3)  # 1.66666667

print(5//3)  # 1    몫만
print(6//3.0)  # 2.0    실수값

print(7 % 4)  # 3   몫을 제외한 나머지 연산자
print(2**3) # 8     거듭제곱    (2**1000) 2의 1000승

print(int(3.3)) #   3  정수로 만들어준다.
print(int(5/2))  # 2

print('10') # 일영 문자 :
print(int('10')+2)  # int가 일영을 숫자10으로 변환 : 12






# 연습문제 1

# 1. 첫 번째 와 셋 째 문자를 출력하세요.
letters = 'python'
print(letters[0]+letters[2])

# 2. 뒤에 4자리만 출력하세요.
cn="24가 2210"
print(cn[-4:])

# 3. 문자열에서 '파'만 출력하세요.
s = "파이썬파이썬파이썬"
print(s[0]+s[3]+s[6])

# 4. 문자열 '720'를 정수형으로 변환해보세요.
num_str = '720'
num_int = int(num_str)
print(num_int)

# 5. 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
data = "15.79"
data = float(data)
print(data)

# 6. 에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요.
fee = 48584
month = 36
print(fee*month, "원")



# Day 3












