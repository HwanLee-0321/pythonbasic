import pandas as pd
from common.connection import connection

# Back-end 패턴
# 1. Controller → 2. Service → 3. DAO → 4. Database

# Service단
#  - 실제 비즈니스 로직 기능을 구현

# 전체 도서 조회(ALL)
def get_books():
    conn = connection()
    try:
        curs = conn.cursor()
        sql = """
            SELECT * FROM tbl_book;
        """
        curs.execute(sql)             # SQL 실행
        rows = curs.fetchall()        # SQL 실행결과 받기  
        rows = pd.DataFrame(rows)     # 2차원 DataFrame 형태로 변환
        
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()
    
    return rows
# 도서 검색
def search_books(keyword: dict):
    pass
# 도서 등록
def insert_books(book:dict):
    pass
# 도서 수정
def update_book(book: dict):
    pass
# 도서 삭제
def delete_book(book_inbn: dict):
    pass