from datetime import datetime, timedelta
import time

# 날짜 포맷팅
# now_date = datetime.now() # 출력 : 2024-10-10 12:05:51.968030
now_date = datetime.now().strftime("%Y.%m.%d %H:%M") # 출력 : 2024.10.10 12:08
print(now_date)     # 현재날짜 및 시간출력

# 날짜 계산
#  ex) 현재 시간에서 13시간 빼기
now = datetime.now() # 현재시간
before_time = (now-timedelta(hours=13)).strftime("%Y.%m.%d %H:%M")
print(before_time)

# 실행시간 계산하는 코드
start_time = time.time()
# → 실행코드
end_time = time.time()
execution_time = end_time - start_time
print(f"실행 시간 : {execution_time} 초")

# 스케줄러(Scheduler)
#   - 일정시간에 반복적으로 동작해야하는 작업
#    ex) 12시간에 한번씩
#        5분에 한번씩
# Python은 유명한 스케줄러 라이브러리 2개
#  1. Scheduler
#   - 매우 쉽고, 매우 기능이 약해
#  2. APScheduler
#   - 매우 쉽고, 기능이 강해

# ** APScheduler
#  1. BlockingScheduler     → 내가 메인이야, 나만 동작할거야
#  2. BackgroundScheduler   → 난 서브야, 뒤에서 동작하고 있을게

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
#sched = BlockingScheduler()
sched = BackgroundScheduler()

# ※ 백그라운드 스케줄러는 반드시 메인 프로그램이 동작 중이여야만 동작함

# 2. Job 생성(함수)
def print_hello():
    print("Hello")
    
# 3. 스케줄러에 Job 등록
#   - CRON 표기법: 날짜 또는 특정시간 표기법
sched.add_job(print_hello, "cron", hour="12", minute="28", id="chosun")

# 4. 스케줄러 실행
sched.start()

