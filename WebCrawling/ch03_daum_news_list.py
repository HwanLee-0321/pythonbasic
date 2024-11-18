import requests
from bs4 import BeautifulSoup
from fnc_news import get_news_info

url = "https://news.daum.net/breakingnews/digital"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# HTML → 하이퍼링크(a 태크 href 속성)

link_list = doc.select("ul.list_news2 a.link_txt")
print(len(link_list))
for i, link in enumerate(link_list):
    print(f"{i+1}=========================================")
    get_news_info(link["href"])