# 데이터베이스 선택
use chosun;  # 대문자: sql 문법, C언어처럼 문자마다 세미콜론 필요

# 테이블 삭제
# - cascade(연쇄반응) + DROP = 연쇄 삭제
#   ㄴ 관련있는거 모두 삭제

drop table if exists tbl_news cascade;

# 테이블 생성
# STRING(문자열) → CHAR, VARCHAR
#  - CHAR(10)         → |a|b|c| | |: 메모리잡아먹고 있음
#  - VARCHAR(10)      → |a|b|c|    : 메모리 안 잡아먹음
#  → VARCHAR(200) ?
#     (200) → 해당 컬럼 입력값의 최대 길이(Byte)

# 영문(2byte), 한글(3byte)
# 고정길이 문자열 → CHAR
# 가변길이 문자열 → VARCHAR
# DATETIME → 날짜(년월일시분)
# AUTO_INCREMENT → 자동으로 COUNT(+1) 값 입력
# PRIMARY KEY(PK) → 테이블의 모든 값을 유일하게 식별
CREATE table if not exists tbl_news(
	id        INT AUTO_INCREMENT PRIMARY KEY,
	title     VARCHAR(200),
	writer    VARCHAR(50),
	content   VARCHAR(10000),
	regdate   VARCHAR(50) 
);

# 테이블 조회
select * from tbl_news;