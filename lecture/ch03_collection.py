# 변수: 하나의 값을 저장할 수 있는 메모리 공간
# 배열: (동일한 자료형의) 여러 값을 저장 할  수 있음
#  - 동일한 자료형만 저장 가능
#  - 고정된 크기 사용 (메모리를 비효율적으로 사용)
#  - 예) 배열 100칸 생성 -> 2개의 값만 저장, 98개는 Empty(사용 X)
#  -     그럼에도 불구하고 100칸을 모두 유지(고정)
# 컬렉션 프레임워크
#  - List, Dictionary(Dict), Set, Tuple

#  - 순서가 있는 자료형(인덱스) : List, Tuple   ex) 기차
#  - 순서가 없는 자료형 : Dict, Set             ex) 가방

# 1. 리스트(List)
#   + [] 사용
#   + 시퀀스 자료형(연속 된 값 저장)
#   + index 사용(슬라이싱 가능) ex) [], [:]
#   + 정렬 가능
#   + mutable(최초 생성 된 후 변경 가능)
#   + packing과 unpacking 가능
#   + 멤버함수: append(), extend(), insert(), remove(), pop(), index(), sorted(), etc..
#   * 2차원 리스트는 표(Table) 형태와 동일

list_a = [] # 빈 리스트
list_b = [1, 2, 3]
list_c = [1, 0.1, "chosun", True]

list_d = ["A", "B", "C"] # Packing
a, b, c = list_d         # UnPacking
# a, b, c = ["A", "B", "C"]

#   가. append()    : 맨 마지막에 값을 추가
a = [1, 2, 3]
a.append(4)
print(a)

#   나. insert()    : 원하는 인덱스에 값을 추가 뒤로 밀어버림
a.insert(1, 9)
print(a)

#   다. extend()    : 리스트와 리스트를 병합
b = [1, 2, 3]
c = [3, 4, 5]
b.extend(c) 
print(b)
# print(b + c)

#   라. remove()    : 값으로 삭제
d = [1, 2, 3]
d.remove(2)
print(d)

#   마. pop()       : 인덱스로 삭제
val = d.pop(0)
print(d)
print(val)      # 리스트에서는 삭제되지만 변수에 담아 값을 유지

#   바. index()     : 원하는 값의 인덱스를 출력
e = ['a', 'b', 'c']
print(e.index('a'))

#   사. sorted()    : 정렬
#       + sort() -> 원본 값을 정렬( 원본값 손실 )
#       + sorted() -> 복제 한 후 값을 정렬( 원본 값 유지 )
#       + 정렬(기본: 오름차순(ASC)), 내림차순(DESC)
f = [99, 50, 30, 10 ,40]
print(sorted(f))    # 기본 : 오름차순(ASC)
print(sorted(f, reverse=True)) # 내림차순(DESC)

# 2. 튜플(Tuple)
#   + 시퀀즈 자료형
#   + index 사용(슬라이싱 가능)
#   + packing, unpacking 가능
#   - (), () 생략가능
#   - immutable(생성 된 후 변경 불가능)
#   - 멤버함수 X, 정렬 불가
#   * 함수 return 값으로 활용

a = (1, 2, 3)   # 튜플
b = 1, 2, 3     # 튜플
c = (5)         # 튜플
d = 5           # int형 (튜플X)
e = 5,          # 튜플 

# 3. 딕트(Dictionary)
#   - {} 사용
#   - 인덱스 없음
#   - {key:value} -> key value pair
#   - value(실제값) -> key값으로 특정
#   - vlaue(중복 가능), key(중복 X) -> 유니크
#   - value는 key로만 접근이 가능함
#   * JSON: 값을 전달할 때 포맷 기준! == Dict

intro = {
    "이름" : "방승우",
    "나이" : "36",
    "전공" : "컴퓨터공학"
}
print(intro["이름"]) # key 값으로 value를 꺼냄
# key 없음 -> 생성
# key 있음 -> 수정
intro["성별"] = "남자"          # Dict 값 추가
intro["전공"] = "소프트웨어"    # Dict 값 수정
print(intro)

# update(): 두 딕트 병합
#   - 병합 시 중복되는 key 가 있다면
#     매개변수로 전달되는 key 값이 overwrite 됨
a = {'a': 1, 'b' : 2}
b = {'b': 5,'c': 3, 'd' : 4}
a.update(b)
print(a)

# pop()
a.pop('b')  # key 값 삭제
print(a)

# in()
#   - key 값이 존재하는지 확인
print(2 in a) # True or False

# Value Access( 값 접근 )

print(intro['이름'])        # "이름" key의 value 호출(값이 없으면 Error)
print(intro.get('이름'))    # "이름" key의 value 호출(값이 없으면 None 전달)

#print(intro.keys())     # Key 값만 추출
#print(intro.value())    # Value 값만 추출
#print(intro.items())    # Key, Value 추출 

# 4. 세트(Set)
#   + 수학의 집합과 동일
#   + {} 사용
#   + 인덱스 없음
#   + 중복값 허용 X
a = {1, 2, 3, 4, 5} # 세트
print(a)

list_f = [1, 2, 3, 3, 5, 5, 7]
print(list_f)

# list_f 에서 중복값을 제거!(리스트)
print(list(set(list_f)))

a = {}  # dict
print(type(a))

# 숙제: a 변수와 b 변수의 값을 교환
a = 10
b = 20

a, b = b, a
print(f"{a} {b}")   