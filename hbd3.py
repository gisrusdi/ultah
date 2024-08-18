import streamlit as st
from streamlit.components.v1 import html
from urllib.parse import quote_plus
import time

# Pengaturan halaman
st.set_page_config(page_title="Ucapan Ulang Tahun", page_icon="🎉", layout="centered")

# Menambahkan musik latar belakang
audio_file = open("music.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3', loop=True, autoplay=True)

# Judul ucapan ulang tahun
st.markdown("<h1 style='text-align: center; color: blue;font-size: 50px;'>Selamat Ulang Tahun!</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: grey;font-size: 20px;'>Untukmu wanita yang aku sayang</h2>", unsafe_allow_html=True)

# Menambahkan balon-balon
html_balloons = """
<script>
  function createBalloon() {
    var balloon = document.createElement("div");
    balloon.className = "balloon";
    balloon.style.backgroundColor = randomColor();
    balloon.style.left = Math.random() * 100 + "vw";
    balloon.style.animationDuration = Math.random() * 3 + 2 + "s";
    document.body.appendChild(balloon);
    setTimeout(() => balloon.remove(), 5000);
  }

  function randomColor() {
    return `hsl(${Math.random() * 360}, 70%, 50%)`;
  }

  for (let i = 0; i < 1000; i++) {
    setTimeout(createBalloon, i * 100);
  }
</script>

<style>
  .balloon {
    width: 20px;
    height: 30px;
    position: absolute;
    bottom: -50px;
    border-radius: 0 0 50% 50%;
    animation: floatUp 5s ease-in infinite;
  }

  @keyframes floatUp {
    0% {transform: translateY(0);}
    100% {transform: translateY(-100vh);}
  }
</style>
"""
html(html_balloons)

# Menampilkan foto
st.image("foto.png", caption="Selamat ulang tahun untukmu, wanita yang paling aku sayang. tiada kata yang bisa aku ucapkan kecuali rasa syukur karena telah mengenal kamu", use_column_width=True)

# Ucapan
st.markdown("<h2 style='text-align: center;'>Sekali lagi! Selamat ulang tahun sayangkuuu hihi 😍</h2>", unsafe_allow_html=True)

# Mengelola state untuk setiap tombol
if "clicked_1" not in st.session_state:
    st.session_state.clicked_1 = False

if "clicked_2" not in st.session_state:
    st.session_state.clicked_2 = False

if "clicked_3" not in st.session_state:
    st.session_state.clicked_3 = False

if "clicked_4" not in st.session_state:
    st.session_state.clicked_4 = False
# Tombol pertama
if st.button("Klik disini ya sayang ❤️") or st.session_state.clicked_1:
    st.session_state.clicked_1 = True
    st.balloons()
    st.image("IMG_20240804_192700_116.jpg")
    text1 = """
    Selamat ulang tahun ya! 

    Aku bersyukur banget bisa ada di samping kamu sampai hari ini. Melihat kamu tumbuh dan berubah menjadi versi terbaik dari dirimu sendiri adalah hadiah terbesar buat aku. Kamu lebih dewasa, lebih bijaksana, dan lebih kuat dari sebelumnya, dan itu bikin aku semakin yakin sama kita. 

    Aku harap aku bisa terus menjadi alasan di balik senyum kamu, tempat kamu pulang di saat suka dan duka. Doaku, semoga kamu selalu diberi kesehatan, panjang umur, dan kebahagiaan di setiap langkah yang kamu ambil. Meskipun tahun ini kita masih berjuang bersama - sama, aku yakin di ulang tahun berikutnya, kita akan merayakannya sebagai pasangan yang halal. 

    Terima kasih sudah menjadi yang terbaik buat aku, dan aku janji akan selalu ada buat kamu. 

    Selamat ulang tahun, sayang! ❤️
    """
    text1_html = text1.replace("\n", "<br>")
    st.markdown(f"<h2 style='text-align: justify; color: grey;font-size: 15px;'>{text1_html}</h2>", unsafe_allow_html=True)

    # Tombol kedua
    if st.button("Klik Lagi yaa 😘 ") or st.session_state.clicked_2:
        st.session_state.clicked_2 = True
        st.image("IMG-20240623-WA0027.jpg")
        text2 = """
        Satu hal yang selalu aku syukuri adalah bisa mengenalmu di dunia ini.

        Kamu wanita yang cantik, ceria, dan penuh semangat. Setiap hari bersamamu adalah anugerah yang tak pernah membuat aku bosan. Senyummu, tawamu, dan caramu membawa kebahagiaan dalam hidupku membuat aku semakin yakin setiap harinya. Walaupun terkadang rasa amarah turut menyertai tapi itu membuat aku semakin tersadar bahwa kalau kamu begitu menyayangi aku hihi.

        Dari awal aku mengenalmu hingga sekarang, satu hal yang tak pernah berubah adalah keinginanku untuk menjadikan wanita cantik ini sebagai istri aku.

        Aku harap kita bisa terus bersama, sampai pada akhirnya kita bisa menjalani hidup sebagai sepasang suami istri yang bahagia. ❤️
        """
        text2_html = text2.replace("\n", "<br>")
        st.markdown(f"<h2 style='text-align: justify; color: grey;font-size: 15px;'>{text2_html}</h2>", unsafe_allow_html=True)
        
        # Tombol ketiga
        if st.button("Klik lagi 🥳 ") or st.session_state.clicked_3:
            st.session_state.clicked_3 = True
            st.image("IMG-20240607-WA0002.jpg")
            text3 = """
            Rasanya senang sekali bisa melihat senyummu, sayang. Meski aku tahu aku belum selalu bisa menjadi pria yang setiap saat membuatmu bahagia, tapi percayalah, dari lubuk hati yang paling dalam, aku selalu berusaha sekuat mungkin untuk mewujudkannya.

            Aku tahu aku bukan orang yang sempurna, tapi izinkan aku terus mencoba. Maafkan aku jika pernah membuatmu bersedih. Aku sungguh berharap, mulai hari ini dan seterusnya, tak ada lagi air mata yang jatuh karena kata-kata, perbuatan, atau sikapku. Hatiku ikut hancur setiap kali melihatmu menangis.

            Sekarang, coba kamu pejamkan matamu, dan doakanlah semua yang kamu harapkan.          
            """
            text3_html = text3.replace("\n", "<br>")
            st.markdown(f"<h2 style='text-align: justify; color: grey;font-size: 15px;'>{text3_html}</h2>", unsafe_allow_html=True)
            if st.button("Terakhir") or st.session_state.clicked_4:
                st.session_state.clicked_4 = True
                st.markdown(f"<h2 style='text-align: center; color: black;font-size: 20px;'>Aamiin ya rabbal alamin, sayangku. 🌹</h2>", unsafe_allow_html=True)
                st.markdown("<h3 style='text-align: center;font-size: 20px;'>🎂 Happy 26 sayangku! 🎂</h3>", unsafe_allow_html=True)
