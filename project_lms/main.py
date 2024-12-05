# streamlit run project_lms/main.py
from service import book_service
import streamlit as st
import pandas as pd

#################
## 1. 초기 설정 ##
#################

# st.session_state["page"] → 현재 사용하고 있는 페이지
# 1. Main Page
# 2. Insert(등록) Page
# 3. Update(수정) Page
if "page" not in st.session_state:
    st.session_state["page"] = "main"

# 다른 페이지로 이동하는 함수
def navigate_to(page):
    st.session_state["page"] = page
    st.rerun()

# 디자인
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 55rem !important;
        }
        hr {
            margin: 0;
            padding: 0;
        }
        .stButton>button {
            width: 5rem;
            padding: 0;
            margin: 0;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        .stColumns {
            gap: 0px; /* 열 간의 기본 간격을 없애기 */
        }
    </style>
""", unsafe_allow_html=True)

###############
## 2. HEADER ##
###############
st.title("도서관리시스템")
st.markdown("<hr>", unsafe_allow_html=True)

if st.button("HOME"):
    navigate_to("main")

if st.button("등록"):  # 만약 등록버튼을 클릭하면?
    navigate_to("insert")  # insert값을 전달
st.markdown("<hr>", unsafe_allow_html=True)

#############
## 3. PAGE ##
#############
def main_page():
    # [전체 도서 데이터 조회]
    rows = book_service.get_books()
    
    # [도서 검색]
    with st.form("search_form"):
        keyword = st.text_input("도서검색")
        submitted = st.form_submit_button("검색")
        if submitted:
            rows = book_service.search_books(keyword)
            st.write(f'"{keyword}"로 검색한 결과는 총 {len(rows)}건 입니다.')

    
    event = st.dataframe(rows,
                         on_select="rerun",  
                         selection_mode="single-row",
                         use_container_width=True,
                         hide_index=True)

def insert_page():
    pass

def update_page():
    pass

#####################
## 4. PAGE CONTROL ##
#####################

if st.session_state["page"] == "main":
    main_page()
if st.session_state["page"] == "insert":
    insert_page()
if st.session_state["page"] == "update":
    update_page()