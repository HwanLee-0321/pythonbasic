# 테이블 생성 SQL
#	- CHAR(문자)
#	- VARCHAR(가변문자)
#	- VARCHAR(500) → Byte 크기

#	- CHAR(10)		→ 문자열의 길이가 고정
#	- VARCHAR(10)	→ 문자열의 길이가 변동일때
#	- Datetime		→ 날짜(년월일시분)
#	- Primary Key(PK 키)
#	   ㄴ 테이블안의 모든 데이터를 유일하게 식별할 수 있는 값

USE chosun

# 테이블 삭제
#	- CASCADE : 연쇄반응
#	예) 게시판 테이블
#		ㄴ 댓글 테이블
DROP TABLE IF EXISTS tbl_news CASCADE;

CREATE TABLE tbl_news(
	id       INT AUTO_INCREMENT PRIMARY KEY,
	title    VARCHAR(200),
	writer   VARCHAR(50),
	content  VARCHAR(10000),
	regdate  VARCHAR(50)
);

#테이블 조회(모든 데이터)
SELECT  * FROM tbl_news