import streamlit as st
from streamlit_option_menu import option_menu

with open("/var/www/html/pages/index.html","r") as f:
    html_index = f.read()

with open("/home/masayosi/python/mainpages/pages/about.html","r") as f:
    html_about = f.read()

with open("/home/masayosi/python/mainpages/pages/access.html","r") as f:
    html_access = f.read()

with open("/home/masayosi/python/mainpages/pages/read_home.html","r") as f:
    html_read_home = f.read()

with open("/home/masayosi/python/mainpages/pages/write.html","r") as f:
    html_write = f.read()

with open("/home/masayosi/python/mainpages/pages/contact.html","r") as f:
    html_contact = f.read()
    print(html_contact)

with open("/home/masayosi/python/mainpages/pages/log_in.html","r") as f:
    html_log_in = f.read()

with st.sidebar:
    selected = option_menu(
menu_title="メインメニュー",
options=["ホーム","our vision","ユーザー登録","レコメンド", "投稿する","お問い合わせ","ログイン","ログアウト"],
)

if selected=="ホーム":
    st.markdown("[ホーム](/var/www/html/pages/index.html)",unsafe_allow_html=True)
if selected=="our vision":
    st.markdown("[our vision](/var/www/html/pages/about.html)",unsafe_allow_html=True)
if selected=="ユーザー登録":
    st.markdown("[ユーザー登録](html_access)",unsafe_allow_html=True)
if selected=="レコメンド":
    st.markdown("[レコメンド](html_read_home)",unsafe_allow_html=True)
if selected=="投稿する":
    st.markdown("[投稿する](html_write)",unsafe_allow_html=True)
if selected=="お問い合わせ":
    st.markdown("[お問い合わせ](html_contact)",unsafe_allow_html=True)
if selected=="ログイン":
    st.markdown("[ログイン](html_log_in)",unsafe_allow_html=True)
if selected=="ログアウト":
    st.markdown("[ログアウト](html_index)",unsafe_allow_html=True)
