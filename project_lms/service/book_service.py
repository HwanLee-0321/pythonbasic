import pandas as pd
from common.connection import connection
# Back-end 패턴
# 1. Controller → 2. Service → 3. DAO → 4. Database

# Service단
#  - 실제 비즈니스 로직 기능을 구현
# 전체 도서 조회(ALL)

# Web개발 패턴 → MVC, MVT, .. 등등
#  - MVC(Model + View + Controller)

# 웹 브라우저(클라이언트) → Request(https://naver.com/blog + 글작성)
# 네이버 웹 서버 → Response(HTML, 정보들을 웹 브라우저에게 전달)
# 1. Controller
#   → 사용자의 Request 받기
#   → 분석 후 "blog" 비즈니스 로지을 처리하는 Service단으로 전달
# 2. Service
#   → 요청 받은 내용의 비즈니스 로직을 처리
#   → 비즈니스 로직을 처리중, DB가 필요한 경우 DAO로 전달
# 3. DAO(Data Access Object)
#   → BlogDAO
#   → DAO는 DB와 통신하면서 DB작업(CRUD) 작업
#   → DB에서 SQL을 실행한 결과 Service 단으로 전달
# 4. Service
#   → DAO로부터 전달받은 결과를 Controller로 전달
# 5. Controller
#   → Service로부터 전달받은 결과와 View(웹 페이지)를
#     클라이언트에게 전달(Response)

# 겨울방학 숙제
# 1.  SQLD 자격증을 취득
#  - ORM 개발(SQL을 사용하지 않음)
#  - SQL을 알고 있으면 ORM을 더 잘 쓸수 있음
#  - 복잡한 SQL문은 ORM으로 안됨!!(한계가 분명 존재)

# 2. WEB 개발 공부!
#  - 어느 분야로 직업을 정해도 웹개발을 기본적으로 알고 있으면 도움
#  - Python + Web + DB = 프로젝트
#  - Python Web → Django, Flask, FastAPI(개추요)
#  * 실제 회사 Python 웹개발 → Django
#  * FastAPI 추천
#  - 왜 추천?
#  1) 웹개발(Spring-JAVA, Node-JS, Django-Python)
#  2) Django 매우 어려움, FastAPI 매우 쉬움
#  3) Web(Spring-JAVA) + AI(Python)

def get_books():
    conn = connection()
    try:
        curs = conn.cursor()
        sql = """
            SELECT * FROM tbl_book;
        """
        curs.execute(sql)             # SQL 실행
        # DB에서 가져 온 전체데이터 → Dict Type(2차원)
        dict_rows = curs.fetchall()        # SQL 실행결과 받기  
        # Dict Type(2차원) → DataFrame(표) Type 변환
        rows = pd.DataFrame(dict_rows)     # 2차원 DataFrame 형태로 변환
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()
    return rows
# 도서 검색
def search_books(keyword: str):
    conn = connection()
    rows = pd.DataFrame()  # Initialize 'rows' to an empty DataFrame to avoid UnboundLocalError
    try:
        curs = conn.cursor()
        sql = """
            SELECT * FROM tbl_book
            WHERE book_name LIKE %(keyword)s
            OR book_writer LIKE %(keyword)s
            OR book_publisher LIKE %(keyword)s;
        """
        curs.execute(sql, {"keyword": "%" + keyword + "%"})
        dict_rows = curs.fetchall()
        rows = pd.DataFrame(dict_rows)  # Assign the result to 'rows' if successful
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()
    return rows

# 도서 등록
def insert_books(book:dict):
    pass
# 도서 수정
def update_book(book: dict):
    pass
# 도서 삭제
def delete_book(book_inbn: dict):
    pass

