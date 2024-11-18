# 주석(comment): 메모, 실행 X

# 1. 출력함수
#  - ()값을 출력
#  - 변수값 확인 용도로 많이 활용

#  - 문자(Char)     -> C('')
#  - 문자열(String) -> C("")
#  - Python은 "", '' 모두 문자열 (String)
print("Hello")

#  참고 : Escape Code ( 문자열과 함께 사용 )
#  - 문법 (\ + @)
#  - \n ( 한 줄 개행 )
#  - \t (탭, 8칸 공백)
print("Hello\nPython")
print("Hello\tPython")

# 자료형(Type)
#  - Python의 모든 자료형은 객체(Object)
#  - 정수형(int)        : 3, -1, 0
#  - 실수형(float)      : 3.14, 0.0, -2.2
#  - 문자열(String)     : "HI", 'hi
#  - 논리형(boolean)    : True, False

# 형 변환(Type Casting)
#  - Type Casting을 사용하여 값을 원하는 자료형으로 변환
#  - int() -> ()안의 값을 정수형으로 변환
#  - float() -> ()안의 값을 실수형으로 변환
#  - str() -> ()안의 값을 문자열으로 변환
#  * 큰 자료형 -> 작은 자료형 \조심!\ (값의 손실이 생김)

a = 3
b = 3.14
c = "5"
d = "5.15"

print(float(a))
print(str(a))
print(int(b))
print(int(d))   # STR(실수) -> 정수 ERROR 발생!

# None Type
#  - 사용 금지!
#  - Null == None
#   -> NullPointerException( 크리티컬 오류 -> 프로그램 종료 )
#  - 만약에 None 또는 Null -> ""

# 변수 생성 및 초기화
#  - num = 5
#  - Python은 변수 선언시 type을 지정하지 않음! ( 동적 타이핑 언어 )
#  - =(대입 연산자) -> 우측에 값을 좌측에 대입