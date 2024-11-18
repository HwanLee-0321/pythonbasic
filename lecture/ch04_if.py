# 조건문(Condition): if~elif~else
#   - 특정조건을 만족하는 경우 수행할 작업에 사용
#   - 모든 조건은 boolean으로 표현
#   - 조건문의 경우 if, elif, else 블록 내 들여쓰기
#   - 모든 블록문의 시작점의 마지막: (콜론) 추가

"""
if 조건1:
    code
elif 조건2:
    code
elif 조건3:
    code
else : 
    code
"""

# if문 조합식
#  1. if
#  2. if ~ else
#  3. if ~ elif
#  4. if ~ elif ~ else

# 논리 연산자 : AND, OR, NOT
#   - AND: 두 조건이 모두 참인 경우
#   - OR : 하나의 조건이라도 참이면 참
#   - NOT : 참이면 거짓, 거짓이면 참

# 예제: 태어난 년도를 입력하면 
#      [성인, 대학생, 고등학생, 중학생, 초등학생, 어린이] 출력하는 코드를 작성

# input() -> 키보드 값 전달 받음
#   - 문자열 자료형으로 입력받음
born = int(input("태어난 년도: "))   # 사용자의 출생 년도 입력

from datetime import datetime   # 라이브러리(datetime)
now = datetime.today().year     # 현재 날짜(년도)

while(now < born):
    born = int(input("잘못된 입력입니다 다시 입력하세요: "))
age = now - born + 1

category = ['성인', '대학생', '고등학생', '중학생', '초등학생', '어린이']

if(age > 26):
    age_category = 0
elif(age >= 20):
    age_category = 1
elif(age >= 17):
    age_category = 2
elif(age >= 14):
    age_category = 3
elif(age >= 8):
    age_category = 4
else:
    age_category = 5

print(f"당신의 출생년도는 {born}년으로 현재 {age}살, {category[age_category]}입니다.")
