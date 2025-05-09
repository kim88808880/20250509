import streamlit as st

st.title("🎈20250509")
st.info(
    "안녕하세요"
)
st.write(
    "반갑습니다."
)
st.image("https://th.bing.com/th/id/R.94cdc1cddbebbdf5dccd68f523f83972?rik=R6J1sNM7nyFLwg&riu=http%3a%2f%2fwww.hancinema.net%2fphotos%2ffullsizephoto249921.jpg&ehk=iW5siMlhFfdKQVJajfaodxn2MU%2bMV7084O4yQ%2fnNCnM%3d&risl=&pid=ImgRaw&r=0")
st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjNhZ2JkZjZncDFvYzdtdTkxcm95Nmd2cm8wNDBqczFvbHdmbWdsNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lv2VhwHrt6ljhvZ6LF/giphy.gif")

st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")

st.link_button("연결할 url을 이 다음 변수에 써주세요!", 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet')

# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성

    # st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("선택한 옵션:", option)

name= st.text_area("이름을 입력해주세요요")
if name =="고구마":
    st.write(name,"님 안녕하세요")
else:
    st.write("고구마님이 아니네요..")

# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)

