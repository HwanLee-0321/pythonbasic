# 절차지향 프로그래밍 언어 -> C,C++
# 객체지향 프로그래밍 언어 -> Python, Java
# 함수지향 프로그래밍 언어 -> Go, Rust

# 객체지향 프로그래밍(OOP)
#  - 객체 → class
#             ㄴ 필드(변수)
#             ㄴ 메서드(함수)

# 완벽한 OOP -> Java -> Class 없으면 개발 불가
# 나머지, 객체지향하고싶은 언어
#  -> 변수, 함수만 사용하다가 객체가 필요한 경우에만 Class 사용

# 함수(Method, Function)
#  - 어떤 일을 수행하는 코드 묶음
#  - 반복적으로 동작해야 하는 일들!

# ** 함수개발 가이드라인 **
#  1. 함수 이름 및 내용
#   - 함수 이름에 함수의 역할과 의도 명확히 드러낼 것!
#   - 함수 내용은 가능하면 짧게 작성

#  2. 함수의 역할
#   - 하나의 함수에 유사한 역할을 하는 코드만 포함
#   - 하나의 함수는 함 가지 기능만 명확히 정의
#   - ex) 계산기(덧셈, 뺄셈, 나눗셈, 곱셈)
#    -> 제곱 기능(곱셈 2번) 
#    -> 곱셈() x 2번 사용 -> 재사용성 Up

#  3. 함수를 만들어야 하는 경우
#   - 공통적으로 사용되는 코드는 함수로 생성
#   - 복잡한 로직이 사용되는 경우 식별 가능한 이름의 함수 생성

# ** 함수의 종류 **
#  1. 내장 함수 (Built-in Function)
#   + 프로그래밍 언어세 기본적으로 제공하는 함수
#   + EX) print(), type(), range(), ...

#  2. 외장 함수 (Library)
#   + 라이브러리: 외부에서 개발해 놓은 코드 묶음
#    가. 라이브러리 설치(아나콘다 pip install ~)
#    나. 라이브러리 호출(from datetime import datetime)
#    다. 라이브러리 사용(datetime.today())
#    .(참조 연산자)

#  3. 사용자 정의 함수  
#   + 개발자가 직접 만들어서 사용하는 함수

# ** 함수 이름 규칙 **
#  - snake_case() 

# Post      -> Class
# post      -> Field
# post()    -> Method

# ** 함수 정의 **
#  1. 기본 함수 문법
#     def 함수명(parameter1, parameter2,...)
#       실행문
#       return 반환값
#     * parameter 와 return은 생략가능

# ** 함수 실습 **
#  1. 함수 사용 방법
#   가. 함수 정의(=생성)
#   나. 함수 호출(=사용)

# 2. 함수 정의
#  + def 키워드 사용 (define)

# 3 함수 호출
#  + 함수 호출 방법은 함수 정의시 만들어진 함수이름을 사용해서 호출
#  + 함수 호출시 입력 매개변수와 함수 정의시 입력 매개변수는 동일한 갯수여야 함
#  || 함수 호출 후 함수 종료 된 경우 "호출 했던 곳"으로 돌아감 ||
#  || 입력 매개변수의 순서가 매우 중요 ||
#  || 최초에는 함수 호출문으로 동작하지만, 함수 종료 후에는 변수로서 활용 됨
#     반환값이 있는 반환값을 담는 변수, 반환값이 없는 경우 None||

# 4. 인자
#  + 매개변수 = parameter = argument
#  + 함수에 전달되는 입력값
#  + parameter 로 int,str, float, list, bool 등 사용 가능
#  + 심지어 함수 또는 클래스를 parameter로 전달 가능
#  + parameter값 2개 이상 사용시 정의 된 순서대로 전달해야 함
#  Tip: 매개변수 10개 전달!
#  def test(a,b,c,d,e,f,g,h,i,j): -> (X)
#  list_val = [a,b,c,d,e,f,g,h,i,j]
#  def test(list_val): -> (O)
#  코드 작성시 종속성은 최대한 배제하면서 개발!
#   -> 종속성: A 코드를 수정하면 B 코드, C 코드도 수정해야하는 경우

# 5. Default parameter 
#  + 함수 정의문과 호출문의 매개변수 갯누는 동일해야함
#   -> 동일하지 않은 경우 Default parameter를 사용해서 기본값을
#      할당 할 수 있음
#  + Default는 맨 뒤 인자부터 사용 가능! 
# def test(a, b, c=3):      # (O)
# def test(a, b=2, c=3):    # (O)
# def test(a=1, b=2, b=3):  # (O)
# def test(a=1, b, c):      # (X)
# def test(a, b=2, c):      # (X)
# def test(a=1, b=2, c):    # (X)

# 6. return
#  + 기본적으로 함수 종료 의미
#  + 함수 종료 2가지
#    가. return 만난 경우
#    나. 함수 블럭문 끝난 경우
#   + return 반환값: 함수 중료 후 호출했던 곳으로 반환값 전환
#   + return 다음에 오는 코드는 실행 안 됨(return 만나면 함수 종료)

# 7. 변수의 범위
#  + 변수가 참고 가능한 코드상의 범위를 명시
#  + 함수 내의 변수는 자신이 속한 코드 블록이 종료되면 소멸
#  + 이렇게 특정 코드블럭에서 선언된 변수를 지역변수
#  + 가장 상단에 정의되어 프로그램 종료 전까지 유지되는 변수를 전역 변수
#  + 같은 이름의 직엽변수과 전역변수가 존재하는 경우 가까운 곳이 우선순위 높음


# **함수 내에서 함수 밖의 전역변수를 변경하는 방법
#  1. global 사용하기
#   + global -> 전역변수를 지칭
#   + global 절대 사용 금지!

# return문 사용
num1 = 10
def test(num1):
    num1 = 99
    return num1

num1 = test(num1)
print(num1)

# 8. 가변길이인자(Variable lenght parameter)
#  + 전달되는 parameter의 갯수가 고정적이지 않는 경우
#  가. *args      -> Tuple
#  나. **kwargs   -> Dict
# range(1, 11, 2)
# range(10)
# range(0,3)

def test(*args):
    for item in args:
        print(item)
test(10,20,30)
test(10)
test(1,2,3,4,5)

def test2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
test2(a=1, b=2, c=3)


# 9. Type hint
#  + 함수의 parameter와 반환값의 자료형 타입을 명시(힌트)
#  + 코드 실행과는 무관

def test3(a: int, b: int) -> int:
    return a + b




