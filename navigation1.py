import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
menu_title="メインメニュー",
options=["ホーム","our vision","ユーザー登録","レコメンド", "投稿する","お問い合わせ","ログイン","ログアウト"],
)

if selected=="ホーム":
    st.markdown("[ホーム](/mount/src/webapp/templates/index.html)",unsafe_allow_html=True)
    
if selected=="our vision":
    st.markdown("[our vision](html_about)",unsafe_allow_html=True)
    
if selected=="ユーザー登録":
    st.markdown("[ユーザー登録](html_access)",unsafe_allow_html=True)
    
if selected=="レコメンド":
    st.markdown("[レコメンド](html_read_home)",unsafe_allow_html=True)
    
if selected=="投稿する":
    st.markdown("[投稿する](html_write)",unsafe_allow_html=True)
    
if selected=="お問い合わせ":
    st.markdown("[お問い合わせ](html_contact)",unsafe_allow_html=True)
    
