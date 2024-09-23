# 문자열의 이해(String)
#  - 데이터 분석
#  - 자연어 처리
#  - 유효성 체크(사용자로부터 입력받은 값 체크)

# 1. 문자열 인덱스(index)
#  - 인덱스는 0번부터 시작
#  - 역인덱스는 -1번부터 시작
#  - 공백도 포함
intro = "Hello Python"  # 인덱스(0~11), 역인덱스(-12~-1), 길이(12)

# 2. 문자 추출
print(intro[0])  #H
print(intro[-2])  #o

# 3. 문자열 슬라이싱(문자열 추출)
#  - [시작:끝] 인덱스 쓰기
#  - [2:5] → 2~4 끝 인덱스 -1값 
print(intro[2:7])  # 2~6번
print(intro[:])    # 처음부터 끝까지
print(intro[:7])   # 처음부터 6까지
print(intro[3:])   # 3부터 끝까지

#20240919 17:20:30


# 4. 문자열 함수
#  - len() : 문자열 길이
print(len(intro))

#  - upper() and lower(): 대소문자 변경
print(intro.upper())
print(intro.lower())

#  - replace(): 특정 문자 치환
print(intro.replace("H", "j"))  #"H"를 "J"로 치환

#  - split(): 구분자를 기준으로 문자열 분할(기본값:공백)
print(intro.split())
print(intro.split("o"))

#  - strip(): 문자열의 좌우공백 제거 rstrip(), lstrip()
# "             ccw     " → "ccw"
print(intro.strip())

#  - in(): 특정 문자열 포함하는지 확인(True or False)
print("Hi" in intro)  #False

#  - find() and rfind(): 문자열 내부의 특정 문자 인덱스 출력
intro = "Hello Python"
print(intro.find("H"))       # 0
print(intro.find("Python"))  # 첫 글자 인덱스
print(intro.find("o"))       # 좌 → 우 / 맨 처음 "o"가 등장하는 인덱스 출력
print(intro.rfind("o"))      # 우 → 좌 / 맨 처음 "o"가 등장하는 인덱스 출력
print(intro.find("Hi"))      # -1

# 문제1.  "cherry1004@gmail.com",
#         "cherry01@gmail.com", 
#         "cherry0@gmail.com"에서
#         아이디만 추출하는 코드 작성
data = str(input())
word = list(data.split("@"))
print(word[0])

#문제2. 도메인 추출하는 코드 작성
# www.naver.com
# www.daum.net
# www.google.com
# 도메인만 추출
data = str(input())
word = list(data.split("."))
print(word[1])