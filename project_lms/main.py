# CRUD(등록, 수정, 삭제, 조회, 검색)
# 프로그래밍언어 → 알고리즘 풀이 → 실무(비즈니스 로직)ㄴ
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
            st.write(f'"{keyword}" 으/로 검색한 결과는 총 {len(rows)}건 입니다.')

    
    event = st.dataframe(rows,
                         on_select="rerun",  
                         selection_mode="single-row",
                         use_container_width=True,
                         hide_index=True)
    if len(event.selection["rows"]):
        # 수정, 삭제에서는 사용자가 선택한 값이 필요!
        #  → 사용자가 선택한 idx의 행(row)값을 가져오기
        selected_idx = event.selection["rows"][0]
        book_isbn = rows.iloc[selected_idx]["book_ISBN"]
        book_name = rows.iloc[selected_idx]["book_name"]
        book_writer = rows.iloc[selected_idx]["book_writer"]
        book_publisher = rows.iloc[selected_idx]["book_publisher"]
        book_price = rows.iloc[selected_idx]["book_price"]
        register_at = rows.iloc[selected_idx]["register_at"]
        useyn = rows.iloc[selected_idx]["useyn"]
        
        data = {
            "book_isbn": book_isbn, 
            "book_name": book_name,
            "book_writer": book_writer,
            "book_publisher": book_publisher,
            "book_price": book_price,
            "register_at": register_at,
            "useyn": useyn 
        }
        # data를 Update 페이지에서도 활용하기 위해
        # 공용저장소에 저장!
        st.session_state["data"] = data
        
        if st.button("수정"):
            navigate_to("update")
        if st.button("삭제"):
            # 삭제시 유일하게 식별할 수 있는 값을 사용해서 조건을 주기
            book_service.delete_book(book_isbn)  # DB에서 해당 ISBN의 도서를 삭제
            navigate_to("main")  # 도서 삭제후 최신화된 정보 출력        
            # TIP: INSERT(등록), UPDATE(수정), DELETE(삭제) 후 반드시 refresh
            


def insert_page():
    with st.form("insert_form"):
        book_name = st.text_input("book_name")
        book_writer = st.text_input("book_writer")
        book_publisher = st.text_input("book_publisher")
        book_price = st.text_input("book_price")
        submitted = st.form_submit_button("등록")
        
        book = {
            "book_name":book_name,
            "book_writer":book_writer,
            "book_publisher":book_publisher,
            "book_price":book_price
        }
        
        if submitted:
            book_service.insert_books(book)
            navigate_to("main")
        
        


def update_page():
    # Access data from session state
    row = st.session_state["data"]
    
    st.write("도서 수정")
    # Create a form for updating the book information
    with st.form("update_form"):
        # Populate the form with the existing book details
        book_ISBN = st.text_input("ISBN", value=row["book_isbn"])
        book_name = st.text_input("도서명", value=row["book_name"])
        book_writer = st.text_input("저자", value=row["book_writer"])
        book_publisher = st.text_input("출판사", value=row["book_publisher"])
        book_price = st.text_input("가격", value=row["book_price"])
        register_at = st.text_input("등록일자", value=row["register_at"])
        useyn = st.text_input("사용유무", value=row["useyn"])
        
        # Submit button for the form
        submit_button = st.form_submit_button("수정 완료")
        
        if submit_button:
            # Collect updated values into a dictionary
            updated_book = {
                "book_ISBN": book_ISBN,
                "book_name": book_name,
                "book_writer": book_writer,
                "book_publisher": book_publisher,
                "book_price": book_price,
                "register_at": register_at,
                "useyn": useyn
            }
            # Call the update function from your book service
            book_service.update_book(updated_book)  # Make sure this function is defined
            # After updating, navigate back to the main page
            navigate_to("main")

    

#####################
## 4. PAGE CONTROL ##
#####################

if st.session_state["page"] == "main":
    main_page()
if st.session_state["page"] == "insert":
    insert_page()
if st.session_state["page"] == "update":
    update_page()