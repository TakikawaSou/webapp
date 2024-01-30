import streamlit as st
from streamlit_option_menu import option_menu

with open("https://boosttest-mainpages-s2qy2vl9pnpwh5lkw5xx99.streamlit.app/","r") as f:
    html_index = f.read()
with st.sidebar:
    selected = option_menu(
menu_title="メインメニュー",
options=["ホーム","our vision","ユーザー登録","レコメンド", "投稿する","お問い合わせ","ログイン","ログアウト"],
)

if selected=="ホーム":
    st.markdown("[ホーム](html_index)",unsafe_allow_html=True)
