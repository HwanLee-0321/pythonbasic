# 다음 뉴스 수집기

# 웹 사이트
#   - 화면 : 뉴스 카테고리를 선택 (stremalit)
#   - 수집 : 뉴스 수집 (requests, beautifulsoup)
#   - 화면 : 출력, 엑셀 (다운로드)(streamlit, pandas)
#   - 저장 : 데이터베이스 저장 (pymysql + MariaDB)
import streamlit as st
from fnc_service import collect_news

# README.md → md(Markdown) 문서

# streamlit run project_collector/main.py
#   ㄴ emoiji(아이콘) → https://snskeyboard.com/emoji/
# Streamlit Doc → https://docs.streamlit.io/


def main():
    st.set_page_config(
        page_title="뉴스 수집기",                         # 웹사이트 제목
        page_icon="project_collector/img/favicon.png"    # 웹사이트 파비콘
    )
    st.title("NEWS :blue[COLLECTOR]")
    st.text("DAUM 뉴스를 수집합니다.")
    with st.form(key='form'):
        submitted = st.form_submit_button("수집")
        
    # 버튼 이벤트 → 수집 버튼을 클릭했을 때 
    if submitted:
        collect_news()   

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    