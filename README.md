## 1. 개발환경 구축

### 1-1. 다운로드
- anaconda
- vscode

### 1-2. 아나콘다 환경세팅
- *실행하면 (base) 가상환경 자동 접속 됨
- conda env list                    (가상환경 목록 확인)
- conda create -n dev python=3.11   (가상환경 생성)
- conda activate dev                (가상환경 접속)
- pip list                          (설치 된 라이브러리 목록 확인)
- pip install [라이브러리]           (설치 된 라이브러리 목록 확인)
- cls

### 1-3. VSCODE 세팅
1. extensions 설치
    - python
    - prettier
    - python extension pack
    - Atom Material Icons
    - Atom Material Theme
2. Settings
    - [Mouse Wheel Zoom] 켜기
    - 
### 1-4. 명령어 단축키
- [ctrl] + [`] : 터미널 켜기
- [ctrl] + [,] : Settings 켜기
- [ctrl] + [/] : 주석 ( 1 Line ) 토글, 블록 (+ 여러줄 가능 )
- [ctrl] + [F11] : 파이썬 코드 실행 ( 터미널 )

1. 기본 터미널 세팅
2. 터미널 폰트 사이즈 수정
3. python run 단축키 설정

## 2. 데이터 베이스
    - 데이터를 효율적으로 저장하고 관리할 수 있는 프로그램(DBMS)
### 2-1. DBMS(데이터베이스 관리 시스템)
    - 관계형 데이터베이스(RDB): 표 형태, 보안이 중요하거나, 영속성 데이터
    (개인정보, 금융정보,)
        → MariaDB, Oracle, MySQL, PostgreSQL
    - NoSQL: 자유 형태, 대용량 수집 데이터
        → MongoDB

### 2-2. SQL(구조질의어)
    - DBMS에게 명령을 내릴 떄 사용
    - 예 ) SELECE * FROM tbl_user;

### 2-3. DBMS 설치 방법
  1. 로컬 설치(설치파일 다운로드 직접 설치)
  2. 클라우드 사용(AWS, GCP, Azure, 기타등등)
  3. 도커 컨테이너

### 2-4. 데이터베이스 구조
  1. DBMS → MariaDB, Oracle, MySQL, PostgreSQL
  2.  ㄴ Database → chosun
  3.       ㄴ Table → tbl_news
  - 프로젝트별로 Database 생성
  - Database(쇼핑몰)
  -     ㄴ Table(회원)
  -     ㄴ Table(상품)
  -     ㄴ Table(구매)
  -     ㄴ Table(고객문의)

### 2-5. 프로그래밍언어 - DB 연결
  1. SQL Mapping: SQL을 작성 → 실행 (과거)
  2. ORM(Object Relation Mapping)   (최신)
  - SQL 복잡도 증가! → ORM 한계

### 2-6. SQL 매핑
  1. Connection 맺기(Python - Database)
    - IP, PORT, ID, PW
  2. 일꾼 만들기(cursor 객체)
  3. JOB 만들기 (SQL 작성)
  4. 실행(일꾼-JOB)
  5. 결과


## 3. 도커 (컨테이너)
    - 도커 : 컨테이너 가상화기술을 구현해주는 프로그램
    - 도커 → 도커 엔진 + 도커 이미지
    - 도커 이미지 : 도커 컨테이너 실행을 위한 설계 도면
    - 도커엔진 : 도커 이미지를 바탕으로 컨테이너 실행

### 3-1. 도커 명령어
    - docker ps         # 현재 실행죽인 컨테이너 확인
    - docker images     # 현재 보유하고 있는 컨테이너 이미지 확인
    - docker un         # 도커 컨테이너 실행
    - docker logs [컨테이너 이름] # 해당 컨테이너 로그 확인
    - docker exec -it [컨테이너 이름] /bin/bash # 해당 컨테이너 접속
    ```
    docker run --name mariadb -d -p 3306:3306 -e 
    MARIADB_ROOT_PASSWORD=mariadb mariadb
    - --name mariadb     # 컨테이너 이름
    - -d                 # 데몬 (백그라운드 실행)
    - p 3306:3306        # 포트(외부 : 내부) → 외부 포트(호스트), 내부포트(컨테이너)
    -e MARIADB_ROOT_PASSWORD=mariabd # 환경설정(ROOT암호=mariadb)
    mariadb            # mariadb 컨테이너 실행 → mariadb 이미지 필요
    ```

## 99. 전체 시스템 구조(학습용) - WEB/APP
#  - Client - Sever
#  *Client(고객: 웹 브라우저)
#  *Server(회사: 서비스를 동작하는 컴퓨터)
# Client(naver.com) -> Server(naver) -> Client(소스코드, 이미지, 정보 전달) -> Client(랜더링)

# 구조
# Client -> 네트워크 -> 클라우드 컴퓨팅(ex: AWS)
#                           ㄴ[Server(Linux : 운영체제)]
#                               ㄴ 도커 컨테이너
#                                   ㄴ 데이터 베이스(RDB, NoSQL) + SQL
#                                   ㄴ 프론트엔드(HTML, CSS, JS, React.js, Vue.js)
#                                   ㄴ 백엔드(Spring, FastAPI, Django, Express)
#                                   ㄴ NginX
# + 프로그래밍 언어
# + 디자인 패턴
# + 자료 구조
# + Github(버전 관리 도구)


#                      Server(Linux : 운영체제)
#                         +
#                      Database(데이터 베이스)
#