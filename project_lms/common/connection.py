import pymysql
import pymysql.cursors
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