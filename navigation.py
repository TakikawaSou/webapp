import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
menu_title="メインメニュー",
options=["ホーム","our vision","ユーザー登録","レコメンド", "投稿する","お問い合わせ","ログイン","ログアウト"],
)

if selected=="ホーム":
    st.markdown("[ホーム](index.html)")
if selected=="our vision":
    st.markdown("[our vision](about.html)")
if selected=="ユーザー登録":
    st.markdown("[ユーザー登録](access.html)")
if selected=="レコメンド":
    st.markdown("[レコメンド](read_home.html)")
if selected=="投稿する":
    st.markdown("[投稿する](write.html)")
if selected=="お問い合わせ":
    st.markdown("[お問い合わせ](/home/masayosi/python/pages/contact.html)")
if selected=="ログイン":
    st.markdown("[ログイン](log_in.html)")
if selected=="ログアウト":
    st.markdown("[ログアウト](index.html)")




def main():


    # HTMLを挿入するセクション
    st.markdown("""
<!DOCTYPE html>
<html lang="jp" style="scroll-padding-top:100px;">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Novel.+</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css">    
</head>

<body>
    <!-- NAV -->
    <nav class="navbar sticky-top navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand my-0" href="index.html"><img src="./logo_novel1.png" height="40"></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse fw-bold" id="navbarNav">
                <ul class="navbar-nav ms-auto me-2">
                    <li class="nav-item"><a class="nav-link" aria-current="page" href="index.html">ホーム</a></li>
                    <li class="nav-item"><a class="nav-link" href="about.html">our vision</a></li>
                    <li class="nav-item"><a class="nav-link" href="access.html">ユーザー登録</a></li>
                    <li class="nav-item"><a class="nav-link" href="read_home.html">レコメンド</a></li>
                    <li class="nav-item"><a class="nav-link" href="write.html">投稿する</a></li>
                    <li class="nav-item"><a class="nav-link" href="contact.html">お問い合わせ</a></li>
                    <li class="nav-item"><a class="btn btn-success btn-sm text-white" href="log_in.html">ログイン</a></li>
                    <li class="nav-item"><a class="btn btn-success btn-sm text-white" href="index.html">ログアウト</a></li>
                </ul>
            </div>
        </div>
    </nav>    
</body>
</html>
    """, unsafe_allow_html=True)

# JavaScript
st.markdown("""
    <script>
        // ナビゲーションの表示・非表示を切り替える関数
        function toggleNavigation() {
            var navigation = document.getElementById("navbarNav");
            navigation.classList.toggle("show");
        }

        // ナビゲーションアイコンのクリック時に表示・非表示を切り替える
        document.getElementById("toggleBtn").addEventListener("click", toggleNavigation);
    </script>
""", unsafe_allow_html=True)

# Streamlitアプリのタイトル
st.title("Novel.+")

if __name__ == "__main__":
    main()
