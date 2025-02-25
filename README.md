# 개발 환경 구축

## 1. 다운로드 및 설치
### 1-1. 필수 프로그램 다운로드
- [Anaconda](https://www.anaconda.com/)
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/)

## 2. 아나콘다 환경 세팅
### 2-1. 가상환경 설정
```sh
# 가상환경 목록 확인
conda env list

# 새로운 가상환경 생성 (Python 3.11 기반)
conda create -n dev python=3.11

# 가상환경 활성화
conda activate dev

# 설치된 라이브러리 목록 확인
pip list

# 라이브러리 설치
pip install [라이브러리명]
```

## 3. Visual Studio Code 설정
### 3-1. 확장 프로그램(Extensions) 설치
- Python
- Prettier
- Python Extension Pack
- Atom Material Icons
- Atom Material Theme

### 3-2. 기본 설정
- `Mouse Wheel Zoom` 활성화
- 터미널 기본 폰트 크기 조정
- Python 실행 단축키 설정

### 3-3. 주요 단축키
- `[Ctrl] + [\`]`: 터미널 열기/닫기
- `[Ctrl] + [,]`: 설정 창 열기
- `[Ctrl] + [/]`: 한 줄 또는 블록 주석
- `[Ctrl] + [F11]`: Python 코드 실행 (터미널)

## 4. 데이터베이스
### 4-1. DBMS(데이터베이스 관리 시스템)
#### 관계형 데이터베이스 (RDB)
- **표(Table) 형태의 구조**로 보안 및 영속성이 중요한 데이터 저장
- 예: MariaDB, Oracle, MySQL, PostgreSQL

#### NoSQL
- **자유로운 데이터 저장 방식**, 대용량 데이터 처리에 적합
- 예: MongoDB

### 4-2. SQL(구조적 질의어)
- DBMS에 명령을 내릴 때 사용하는 언어
- 예시:
```sql
SELECT * FROM tbl_user;
```

### 4-3. DBMS 설치 방법
1. **로컬 설치**: 직접 다운로드 후 설치
2. **클라우드 사용**: AWS, GCP, Azure 등
3. **도커 컨테이너 사용**

### 4-4. 데이터베이스 구조
- **DBMS → Database → Table** 형태
- 예시:
  - `chosun` (Database)
    - `tbl_news` (Table)
  - 쇼핑몰 Database 예제:
    - `회원` (Table)
    - `상품` (Table)
    - `구매` (Table)
    - `고객문의` (Table)

### 4-5. 프로그래밍 언어와 DB 연결 방식
1. **SQL 매핑**: 직접 SQL을 작성하여 실행
2. **ORM (Object-Relational Mapping)**: 객체 지향적인 방식으로 데이터 처리 (복잡한 SQL의 한계 있음)

### 4-6. SQL 매핑 과정
1. **연결 (Connection)**: Python → Database
2. **Cursor 객체 생성** (작업 수행자)
3. **SQL 작성** (Job 생성)
4. **SQL 실행** (Cursor와 연결)
5. **결과 반환**

## 5. 도커 (Docker)
### 5-1. 도커 개요
- 컨테이너 가상화 기술을 제공하는 프로그램
- 주요 구성 요소:
  - **도커 엔진**: 컨테이너 실행을 관리
  - **도커 이미지**: 컨테이너 실행을 위한 설계 도면

### 5-2. 주요 도커 명령어
```sh
# 실행 중인 컨테이너 확인
docker ps

# 보유한 도커 이미지 확인
docker images

# 컨테이너 실행
docker run --name [컨테이너명] -d [이미지명]

# 컨테이너 로그 확인
docker logs [컨테이너명]

# 컨테이너 접속
docker exec -it [컨테이너명] /bin/bash
```

### 5-3. MariaDB 컨테이너 실행 예제
```sh
docker run --name mariadb -d -p 3306:3306 -e MARIADB_ROOT_PASSWORD=mariadb mariadb
```
- `--name mariadb` : 컨테이너 이름 지정
- `-d` : 백그라운드 실행
- `-p 3306:3306` : 외부(호스트)와 내부(컨테이너) 포트 연결
- `-e MARIADB_ROOT_PASSWORD=mariadb` : 환경 변수 설정 (ROOT 비밀번호 설정)
- `mariadb` : 사용할 도커 이미지 지정

## 6. 전체 시스템 구조 (WEB/APP)
### 6-1. 클라이언트 - 서버 구조
- **Client (사용자: 웹 브라우저, 모바일 앱) → Server (회사: 서비스 제공)**
- 예시 (naver.com 접속 시):
  - Client(웹 브라우저) → 요청 → Server(naver)
  - Server → HTML/CSS/JS, 이미지, 정보 전송 → Client 렌더링

### 6-2. 웹 시스템 구조
```plaintext
Client → 네트워크 → 클라우드 컴퓨팅 (예: AWS)
                ㄴ 서버 (Linux 운영체제)
                    ㄴ 도커 컨테이너
                        ㄴ 데이터베이스 (RDB, NoSQL) + SQL
                        ㄴ 프론트엔드 (HTML, CSS, JavaScript, React.js, Vue.js)
                        ㄴ 백엔드 (Spring, FastAPI, Django, Express.js)
                        ㄴ 웹 서버 (NginX)
```

### 6-3. 추가 학습 요소
- **프로그래밍 언어**: Python, JavaScript, Java 등
- **디자인 패턴**: MVC, MVVM 등
- **자료 구조 및 알고리즘**
- **버전 관리**: Git, GitHub, GitLab

---

이 문서는 개발 환경을 처음 구축하는 사용자부터 도커와 데이터베이스 관리까지 한눈에 볼 수 있도록 정리되었습니다. 필요에 따라 내용을 확장하여 프로젝트에 맞게 활용하세요!

