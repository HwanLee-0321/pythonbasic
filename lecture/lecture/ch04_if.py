# 제어문
# 1. 조건문
#  - if
# 2. 반복문
#  - for
#  - while

# 조건문(Condition): if~elif~else
#  - 특정조건을 만족하는 경우 수행할 작업에 사용
#  - 모든 조건은 boolean으로 표현
#  - 조건문의 경우 if, elif, else 블록 내 들여쓰기
#  - 모든 블록문의 시작점은 :(콜론)

# if 조건1:
#     실행문
# elif 조건2:
#     실행문
# elif 조건3:
#     실행문
# else:
#     실행문


# if문 조합식
#  1. if
#  2. if ~ else
#  3. if ~ elif ~ elif
#  4. if ~ elif ~ else

# 2개 이상의 조건을 사용하고 싶은 경우
#  - AND, OR, NOT
# 1. AND: 두 조건이 모두 참인 경우 참
# 2. OR: 한 조건이라도 참이면 참
# 3. NOT: 참 -> 거짓, 거짓 -> 참

# 예제) 사용자로부터 출생년도를 입력받고
#       성인, 대, 고, 중, 초, 어린이로 분류하는 코드 작성하세요.


# if n <= 2005:
#     print("성인 및 대학생")
# elif 2005 < n and n <=2008:
#     print("고등학생")
# elif 2008 < n and n <=2011:
#     print("중학생")
# elif 2011 < n and n <=2014:
#     print("초등학생")
# else:
#     print("어린이")
born = int(input("출생년도: "))
print(born)
if born > now:
    print(f"{now}보다 작은 출생년도를 입력해주세요.")
    # 다시 출생년도 입력받기
    
from datetime import datetime
now = datetime.today().year

age = now - born
print(age)

if age >= 27:
    category = "성인"
elif 20 <= age and age <= 26:
    category = "대학생"
elif 17 <= age and age <= 19:
    category = "고등학생"
elif 14 <= age and age <= 16:
    category = "중학생"
elif 8 <= age and age <= 13:
    category = "초등학생"
elif 0 <= age and age <= 7:
    category = "어린이"


print(f"출생년도 {born}, 나이는 {age}로 당신은 {category}입니다.")