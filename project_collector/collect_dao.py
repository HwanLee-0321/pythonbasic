# DAO (Data Access Object)
#   - 실제 Database 와 연결하고 작업하는 내용 (CRUD)

from connection import connection


def insert_news(data: dict):
    conn = connection()
    
    try:
        curs = conn.cursor()
        sql = f"""
            INSERT INTO tbl_news(title, writer, content, regdate) 
            VALUES(%(title)s, %(writer)s, %(content)s, %(regdate)s);
        """
        curs.execute(sql, data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 5. 자원 반납(curs, conn)
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()
        pass
    