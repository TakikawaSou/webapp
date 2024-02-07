import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from pathlib import Path

with st.sidebar:
    selected = option_menu(
menu_title="メインメニュー",
options=["ホーム","our vision","レコメンド", "画像生成"],
)

if selected=="ホーム":
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
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
    <script>
        AOS.init({
            duration: 1000,
            once: true,
        });
    </script>
<!-- css -->
<style>
    .bg-custom-green {
        background-color: rgb(21, 127, 92);
        border-radius: 10px;
        padding: 15px; /* 余白を追加 */
    }

    .rounded-image {
        border-radius: 10%; /* 丸みを帯びさせるために10%を指定 */
        overflow: hidden; /* 余分な部分を非表示にする */
        margin-bottom: 10px; /* 下部の余白を追加 */
    }

    .rounded-image img {
        width: 100%; /* 親要素に対して100%の幅 */
        height: auto; /* 高さは自動調整 */
        object-fit: cover; /* アスペクト比を保ったまま画像を表示 */
    }

    .text-move {
        margin-left: 5px;
        white-space: nowrap;
        line-height: 1.2;
    }
    @media (max-width: 768px) {
    .text-move {
            margin-left: 5px;
            white-space: normal; /* 折り返し可能にする */
            max-height: none; /* 高さの制限を解除 */
            overflow: visible; /* オーバーフローの表示を可能に */
        }
    }
    #novel {
        word-wrap: break-word;
    }
    #novel img {
        max-width: 100%;
        height: auto;
    }
    .text-move {
        white-space: pre-line;
    }
</style>
</head>

<body>
    <!-- 初めに -->
    <div class="content text-black mx-5 mt-3">
        <h3><span class="text-success fw-bold">レコメンド</span>で読者と作家・作品をつなぐ小説投稿サイト　<span class="text-success fw-bold">Novel.+</span></h3>
    </div>

<!-- 作品表示 -->
<h2 id="novel" class="text-dark mt-5 ms-2">注目作品</h2>
<section class="bg-white text-white">
    <div class="row border m-3 bg-custom-green">
        <div class="col-md-3 rounded-image">
            <img src="./app/static/image1.jpg" alt="Your Image"> <!-- 画像を挿入 -->
        </div>
        <div class="col-md-9">
            <h3 class="text-move"><a class="text-white" href="read.html">空へ</a></h3>
            <p class="text-move">あらすじ:<br> 
                高校生の夏休み、天文部員の少年は偶然見つけた古びた望遠鏡で星を観察する。<br>
                不思議な力に導かれ、星座がかたち取る魔法の扉が開かれる。<br>
                彼は友達と共に、星の世界へ飛び込む決断をする。<br>
                未知なる冒険が彼らを待ち受け、夢と冒険が交錯する空の旅が始まる。</p>
        </div>
    </div>
</section>

<section class="bg-white text-white" id="showcases1">
    <div class="row border m-3 bg-custom-green">
        <div class="col-md-3 rounded-image">
            <img src="data:image/png;base64,{image_encoded}" alt="Your Image"> <!-- 画像を挿入 -->
        </div>
        <div class="col-md-9">
            <h3 class="text-move"><a class="text-white" href="read.html">春の出会い</a></h3>
            <p class="text-move">あらすじ:<br>春風が心地よく舞い、桜の花びらが舞い散る季節。新しい出会いの予感が胸に満ちる。<br>微笑みが咲く街で、心と心が繋がる瞬間。<br>春の温かさが、未知の世界への扉を開く。<br>新たな出会いが、人生を彩る幸せな一節の始まりだ。</p>
        </div>
    </div>
</section>

<section class="bg-white text-white" id="showcases2">
    <div class="row border m-3 bg-custom-green">
        <div class="col-md-3 rounded-image">
            <img src="image2.jpg" alt="Your Image"> <!-- 画像を挿入 -->
        </div>
        <div class="col-md-9">
            <h3 class="text-move"><a class="text-white" href="read.html">あなたの心に届けたい</a></h3>
            <p class="text-move">あらすじ:<br>
                孤独なアンドロイドが感情を持ち、人間の心に触れたいと望む。<br>
                彼女は感情データを学ぶ中で、音楽と出会い心を開く。<br>
                ある日、彼女は音楽の力で人々の心に感動と愛を届けることを決意。
                感動の連鎖が始まり、彼女の存在が心に寄り添う。<br>
                アンドロイドの愛と感動が、冷たい鋼鉄の身体を超えて、温かな心を広げていく。
            </p>
        </div>
    </div>
</section>

<section class="bg-white text-white" id="showcases3">
    <div class="row border m-3 bg-custom-green">
        <div class="col-md-3 rounded-image">
            <img src="image3.jpg" alt="Your Image"> 
        </div>
        <div class="col-md-9">
            <h3 class="text-move"><a class="text-white" href="read.html">金魚鉢を眺めながら</a></h3>
            <p class="text-move">あらすじ:<br>
                窓辺の金魚鉢を眺めながら、女性は遠い思い出に浸る。<br>
                幼少の頃、祖母が教えてくれた金魚の名前や不思議な話。<br>
                懐かしい言葉と潤んだ瞳で、彼女は過去と現在をつなぐ。<br>
                金魚の泳ぎが時間の流れを感じさせ、心は穏やかになる。<br>
                窓辺の小宇宙で、彼女は時折り祖母の微笑みを感じ、大切な思い出を静かに抱える。
            </p>
        </div>
    </div>
</section>

<!-- ランキング -->
<div class="text-dark mt-5 ms-2">
    <h1>ランキング</h1>
    

</div>


 <!-- Bootstrapのフッター -->
    <footer class="footer">
        <div class="container text-black text-end my-0">
            <span>© 2023 Novelize Supporter All rights reserved.</span>
        </div>
    </footer>
    
</body>
</html>
""",unsafe_allow_html=True)
    
if selected=="our vision":
    st.markdown("(https://www.kodansha.co.jp/)",unsafe_allow_html=True)
    
if selected=="レコメンド":
    st.markdown("[レコメンド](https://masayoshi-nakagawa.github.io/IseTrip/Isetrip320.html)",unsafe_allow_html=True)
    
if selected=="画像生成":
    st.markdown("[画像生成](html_access)",unsafe_allow_html=True)
