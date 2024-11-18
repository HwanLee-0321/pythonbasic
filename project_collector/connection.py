# PYthon -------- Data Base(MariaDB)
#   - IP
#   - Port
#   - ID
#   - PW

import pymysql
import pymysql.cursors
# 네트워크
#   - IP : 컴퓨터 인터넷 주소

# 집 통신사 → IP 주소(고정, 유동)
# 127.0.0.1 루프백 IP

# Connect to MariaDB
def connection():
    try:
        connection = pymysql.connect(
            host = "127.0.0.1",
            port = 3306,
            user = "root",
            password = "mariadb",
            database = "chosun",
            charset = 'utf8',
            autocommit = True,
            cursorclass = pymysql.cursors.DictCursor
        )
        
        return connection
    except pymysql.Error as e:
        print(f"MARIADB connection failed")