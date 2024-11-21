# 정규식(regex or regexp)
#  → 유효성체크 사용
#  → 원하는 값만 추출

# 유효성체크?
#  → 사용자가 입력한 값이 유효한 값인지 체크
import re

keyword = input("키워드: ")

# 영어대소문자, 한글만 추출(= 그 외 모두 제거)
extract_value = re.sub(r'[^A-Za-z가-힣]', "", keyword)
print(extract_value)