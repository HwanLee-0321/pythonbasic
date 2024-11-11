from datetime import datetime, timedelta
import time


# 1. 날짜 포맷팅(원하는 형식으로 날짜 출력)
#  - %m(월), %M(분)
now = datetime.now().strftime("%Y년 %m월%d일 %H일%M분%S초")
print(now)

# 2. 날짜 계산(현재시간에서 13시간 빼기)
now = datetime.now()
before_time = (now - timedelta(hours=13))
print(before_time)

# 3. 실행시간 계산
start_time = time.time()
# → 실행코드(시간을 알고 싶은)
end_time = time.time()
execution_time = end_time - start_time
print(f"실행시간: {execution_time}초")
