# 주석(comment) : 실행 X, 메모
# 주석 지정 [ctrl] + [/]

print()

# 1. 출력함수(print)
# -() 값을 출력
# -() 변수값 확인 용도로 많이 활용
# C 언어
# - ''(char) - 문자형
# - ""(string) - 문자열
# python
# - '' or "" - 문자열형(String)

print("Hello")  #주석을 달아주세요

# 2. Escape Code(문자열과 함께 사용)
# - \n: 한 줄 개행
# - \t: 탭(기본: 8칸)

print("Hello \tpython") 
print("Hello \npython") 

# 3. 자료형(type)
# - python의 모든 자료형은 객체(Object)
# - 정수형(int)     : 3, -1, 0
# - 실수형(float)   : 3.14, 9.0, -2.2
# - 문자열(String)  : "Hi" , 'hi'
# - 논리형(Boolean) : True, False

# 4. 형 변환(Type casting)
# - 원하는 자료형으로 변환
# - int()
# - float()
# - str()
# - * 큰자료형 -> 작은자료형 변환(조심! 값의 손실이 생김)
# - int("3.14") -> ERROR    

# 5. 변수 선언 및 초기화
# - num = 5
# - type을 정의 하지 않음(동적 타이핑 언어)
# - =(대입연산자) : 우측의 값을 좌측에 대입
# - 초기화: 초기 변수를 생성하면 변수를 생성한 메모리 공간에
#          쓰레기 파일들이 존재, 변수에 값을 대입하면
#          쓰레기 파일들이 삭제(초기화) 돼고 값만 저장
 
 
#  6. 상수
# - 값이 변하지 않음
# - 변수 선언 및 초기화를 항상 함께
# - 전부 대문자 사용!
num = 3         # 변수 
MAX_VALUE = 30  # 상수

# 7. 명명규칙(Naming Rule)
# - 변수, 함수, 클래스 등 사용자 정의 이름에 사용!
# - 명확하고 알아보기 쉽게 작성할 것!
# 
# 1. 영어 대소문자, 숫자, 특수문자(_, -)만 사용!
# 2. 숫자로 시작못함
#   abc123(o) , 123abc(x)
# 3. 영어 대소문자 구별
#   abc != Abc != aBc != abC
# 4. 예약어 사용불가
#   *예약어: 프로그래밍 언어에서 이미 사용하고 있는 이름
#   for, while, if, print, class, return, def, ...
#   굳이 노력해서 쓸려고 하지 마시길...

# 8. 네이미 메서드(Naming Method)
# - 변수, 함수, 클래스 등의 사용자 정의 이름에 가용하는 기법
# - 프로그래밍 언어별로 Naming Method가 다름



# 가. PascalCase (StudentNumber)
# 나. camelCase  (studentNumber)
# 다. snake_case (student_number)
# 라. kebeb-case (student-number)

#           변수            함수            클래스
# JAVA      카멜            카멜            파스칼
# PYTHON    스네이크        스네이크         파스칼

# 9. 동적 출력
student_num = 24
name = "홍길동"

print("조선대학교 24학번 홍길동입니다.")  # 하드코딩(지양)

# 가. format() - old
print("조선대학교 {}학번 {}입니다.".format(student_num, name))
# 나. f-string - new
print(f"조선대학교 {student_num}학번 {name}입니다.")

