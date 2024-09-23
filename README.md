## 99. 전체 시스템 구조(학습용) -WEB/APP
- Client-Server 구조
- *Client: 고객(웹 브라우저)
- *Server: 회사(서비스를 동작하는 컴퓨터)
- A(Client) -> 카톡 -> Server(카카오톡) -> 카톡 -> B(Client)

1. 동작 순서
   + 클라이언트(naver.com) 요청!
   + 네이버 서버(메인 페이지에 필요한 소스들을 전달 -> 클라이언트)
   + 클라이언트 소스 다운로드
   + 클라이언트 렌더링

2. 구조
                    *네트워크*              클라우드 컴퓨팅(AWS)
Client           ->요청(request)       -> Server(LINUX) *운영체제* 
Client(랜더링)    <-전송(response)      <- ㄴ 컨테이너(도커) 
                                            ㄴ 프론트엔트(HTML, CSS, JS, React.js, Vue.js)
                                            ㄴ 백엔드(Spring, FastAPI, Express, Django)
                                            ㄴ 데이터베이스(RDB, NoSQL) + SQL
                                          
*프로그래밍 언어*(Python, Java, C/C++, )
디자인 패턴
*자료구조*
