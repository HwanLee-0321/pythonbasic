# 문자열의 이해(String)
#  - 활용 예: 데이터 분석, 자연어 처리 응용, 사용자로부터 값을 입력받고 처리 (유효성 체크)

# 1. 문자열 인덱스(index)
#  - 문자열은 각 문자마다 순서(인덱스) 있음
#  - 인덱스 시작은 0
#  - 인덱스는 공백 포함
intro = "Hello Python" # index(0~11), length(12), 역인덱스(-12~-1)

# 2. 문자 추출
#  - 인덱스 범위 벗어난 경우(Error: index out of range)
print(intro[0])     # H
print(intro[-2])    # o

# 3. 문자열 슬라이싱(문자열 추출)
#   - [시작:끝]     끝 -1
#   - [0:11] -> 0~10
print(intro[:])     # 처음부터(0) 끝까지
print(intro[:6])    # 처음부터(0) 5 -> 0~5

date ="20243052 12:27" 
print(date[0:4])        # 시험에 나온다

# 4. 문자열 함수

#  - upper() : 대문자로 변환, lower(): 소문자로 변환
print(intro.upper())
print(intro.lower())

#  - replace(): 특정 문자 치환
print(intro.replace("H", "J")) 

#  - split(): 구분자를 기준으로 문자열 분할(기본값: 공백)
print(intro.split())    # 공백을 기준으로
print(intro.split("o")) # o 를 기준으로

#  - strip() : 문자열의 좌우공백 제거
#   ㄴ rstrip(), lstrip()
# "         ccw         " -> "ccw"
print(intro.strip())

#  - in(): 특정 문자열 포함하는지 확인(True or Flase 출력)
print("python" in intro)    # 대소문자 구별(정확히)

#  - find() and rfind() : 문자열 내부의 특정 문자 인덱스 출력
intro = "Hello Python"
print(intro.find('H'))
print(intro.find("Python"))     # 첫번째 글자의 인덱스
print(intro.find("o"))          # 좌측에서 부터 먼저 찾는거
#print(intro.rfine("o"))         # 우측에서 부터 먼저 찾는거
print(intro.rfind("hi"))        # 없는 경우 -1 출력

# 문제1. "cherry1004"만 출력
#  -아이디의 길이는 상시 달라집니다.
#  아이디: "cherry123", "cherry10", "cherry0"
id = "cherry1004@gmail.com"

# 문제2. 도메인 추출
# ex) www.naver.com
#     www.google.com
#     www.daume.net
# naver, google, daum을 추출하는 코드(1가지)