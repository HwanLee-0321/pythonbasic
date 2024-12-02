# 다음 뉴스 수집기
# STREAMLIT(웹사이트) → 수집(실시간 뉴스) → DB에 저장
#                                       → CSV 저장
#                                       → 웹 페이제 데이터 시각화

# 웹 사이트
#   - 화면 : 뉴스 카테고리를 선택 (stremalit)
#   - 수집 : 뉴스 수집 (requests, beautifulsoup)
#   - 화면 : 출력, 엑셀 (다운로드)(streamlit, pandas)
#   - 저장 : 데이터베이스 저장 (pymysql + MariaDB)
import streamlit as st
from project_collector.fnc_service import collect_news
import re

# README.md → md(Markdown) 문서

# streamlit run main.py (main.py 주소 입력)
#   ㄴ emoiji(아이콘) → https://snskeyboard.com/emoji/
# Streamlit Doc → https://docs.streamlit.io/

def convert_df(df):
    return df.to_csv(index=False, encoding='utf-8')

def main():
    st.set_page_config(
        page_title="뉴스 수집기",   # 웹사이트 제목
        page_icon="img/favicon.png"    # 웹사이트 파비콘
    )
    st.title("NEWS: :blue[Collector]")
    st.text("DAUM 뉴스를 수집합니다.") 

    flag = False
    if st.button('수집'):
        df_news, count = collect_news()
        st.write(f"뉴스 {count}건을 수집 완료")
        st.write(df_news)
        flag = True
        news_csv = convert_df(df_news)
    
    if flag:
        st.download_button(
            label="다운로드",
            data=news_csv,
            file_name=f"실시간 뉴스.csv",
            mime="text/csv",
            key="download_csv"
        )

if __name__ == "__main__":
    main()