import streamlit as st
from openai import OpenAI

# 페이지 구성
st.set_page_config(page_title="20250509 AI Assistant", page_icon="🎈", layout="wide")

# 타이틀 및 소개
st.title("🎈 20250509 민짱 홈페이지")
st.info("안녕하세요 👋\n\n이 앱은 다양한 기능을 하나로 모은 데모 페이지입니다.")

st.markdown("---")

# 인사 메시지 및 이미지
st.subheader("💬 반가워요!")
st.write("방가. 아래 이미지를 구경해보세요 👇")

st.image(
    "https://th.bing.com/th/id/R.94cdc1cddbebbdf5dccd68f523f83972?rik=R6J1sNM7nyFLwg&riu=http%3a%2f%2fwww.hancinema.net%2fphotos%2ffullsizephoto249921.jpg&ehk=iW5siMlhFfdKQVJajfaodxn2MU%2bMV7084O4yQ%2fnNCnM%3d&risl=&pid=ImgRaw&r=0",
    caption="📷 이미지 예시",
    use_column_width=True
)


# 사이드바
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("✅ 선택한 옵션:", option)

# 텍스트 입력 예제
st.subheader("🖊️ 사용자 입력")
name = st.text_area("이름을 입력해주세요")

if name == "고구마":
    st.success(f"안녕하세요, {name}님! 😊")
elif name:
    st.info("고구마님이 아니네요..")

# 라디오 버튼
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("🧍 선택한 성별:", gender)

st.markdown("---")

# OpenAI API 사용
st.subheader("🤖 GPT-4o 응답 받기")

user_api_key = st.secrets["openai"]["api_key"]

if user_api_key:
    client = OpenAI(api_key=user_api_key)
    prompt = st.text_input("💬 프롬프트를 입력해주세요")

    if prompt:
        with st.spinner("GPT가 생각 중이에요..."):
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
        st.markdown("### 💡 GPT의 답변:")
        st.success(completion.choices[0].message.content)

# import streamlit as st

# st.title("🎈20250509")
# st.info(
#     "안녕하세요"
# )
# st.write(
#     "반갑습니다."
# )
# st.image("https://th.bing.com/th/id/R.94cdc1cddbebbdf5dccd68f523f83972?rik=R6J1sNM7nyFLwg&riu=http%3a%2f%2fwww.hancinema.net%2fphotos%2ffullsizephoto249921.jpg&ehk=iW5siMlhFfdKQVJajfaodxn2MU%2bMV7084O4yQ%2fnNCnM%3d&risl=&pid=ImgRaw&r=0")
# st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjNhZ2JkZjZncDFvYzdtdTkxcm95Nmd2cm8wNDBqczFvbHdmbWdsNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lv2VhwHrt6ljhvZ6LF/giphy.gif")

# st.code("""
# import streamlit as st
# st.title('Hello World')
# """, language="python")

# st.link_button("연결할 url을 이 다음 변수에 써주세요!", 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet')

# # st.columns(n): 화면을 n개의 수직 열로 나눕니다
# col1, col2 = st.columns(2)  # 2개의 열 생성

# with col1:
#     st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
# with col2:
#     st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성

#     # st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
# st.sidebar.title("📌 사이드바 메뉴")
# option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
# st.write("선택한 옵션:", option)

# name= st.text_area("이름을 입력해주세요요")
# if name =="고구마":
#     st.write(name,"님 안녕하세요")
# else:
#     st.write("고구마님이 아니네요..")

# # 여러 옵션 중 하나 선택
# gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
# st.write("선택한 성별:", gender)

# import openai

# user_api_key = st.text_input("키를 입력해주세요.")

# if user_api_key:
#     from openai import OpenAI

#     client = OpenAI(api_key = user_api_key)
#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     st.markdown("### 💡 GPT의 답변:")
#     st.write(completion.choices[0].message.content)

