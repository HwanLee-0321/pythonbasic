# SELENIUM
#  - 설치: pip install selenium
#  - 웹 크롤링(정적, 동적 모두 가능) + 자동화
#    ㄴ SELENIUM이 제어할 수 있는 웹 브라우저 사용
#    ㄴ 기본적으로 크롬을 씀. 근데! 다른 브라우저도 사용가능.. ex) 마소엣지, 파폭, 브래이브, 유니티 등등
#  - 과거에 웹브라우저 테스트 도구

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 디폴트: SELENIUM 코드 종료 → 웹브라우저 종료!
# 1. 셀레니움 웹브라우저 설정
options = Options()
options.add_experimental_option("detach", True)  # 웹브라우저 종료 X
# options.add_argument("headless")  # 셀레니움 백그라운드 동작(개발 완료)

# ※ 셀레니움이 로봇이 아닌척 하는 방법
options.add_argument("disable-blink-featuers=AutomationControlled")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable=automation"])


# ※ 셀레니움 4버전 이하에서는 ChromeDrvier를 설치해서 사용!
#    4번전부터는 설치할 필요 없음!
#    service = Service(ChromeDriverManager().install())

# 2. 셀레니움 웹브라우저 생성
driver = webdriver.Chrome(options=options)

# 3. 셀레니움 웹브라우저 사용
driver.get("https://www.naver.com")
time.sleep(1)
print(driver.page_source)  # 네이버 메인 페이지의 소스코드 GET

search = driver.find_element(By.ID, "query")    
search.send_keys("정우성")
search.send_keys(Keys.ENTER)
time.sleep(1)

print(driver.page_source)  # 현재 웹브라우저 페이지의 소스코드 GET

# + BeautifulSoup
