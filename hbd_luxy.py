import streamlit as st
from streamlit.components.v1 import html
from urllib.parse import quote_plus
import time

# Pengaturan halaman
st.set_page_config(page_title="Ucapan Ulang Tahun", page_icon="🎉", layout="centered")

# Menambahkan musik latar belakang
audio_file = open("DJ Ulang Tahun (Are U Ready_) (mp3cut.net).mp3", "rb")
audio_bytes = audio_file.read()


# Judul ucapan ulang tahun
st.markdown("<h1 style='text-align: center; color: blue;font-size: 50px;'>Selamat Ulang Tahun Luxyyyyyy 🎉 </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: grey;font-size: 20px;'>Bocil tapi umur udh 25 wkwk</h2>", unsafe_allow_html=True)
st.audio(audio_bytes, format='audio/mp3', loop=True, autoplay=True)
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

  for (let i = 0; i < 10000; i++) {
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
st.image("foto.png", use_column_width=True)

# Ucapan
st.markdown("<h2 style='text-align: center;'>Ini kuenya yaa wkwk, jangan lupa tiup lilinnya 🕯️🎈 </h2>", unsafe_allow_html=True)

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
if st.button("Klik disini untuk hadiah ") or st.session_state.clicked_1:
    st.session_state.clicked_1 = True
    st.balloons()
    st.image("IMG_20240524_094755_092.jpg")
    text1 = """
    Selamat menua, Luxy! 🎉

    Weeeh, tambah tua aja nih, semoga makin bijak dan makin makin lainnya ......
    Semoga semua mimpi dan cita-cita kamu segera tercapai, termasuk yang satu itu—cepat lulus dan cepet nikah, hahaha! 🎓💍

    Tetap semangat menjalani hari-hari, jangan lupa untuk selalu bahagia dan menikmati setiap momen. Terima kasih udah jadi teman yang luar biasa, semoga di tahun yang baru ini, kamu semakin sukses, sehat, dan diberkahi dengan banyak kebahagiaan.
    Nikmati hari spesialmu ini, dan jangan lupa traktiran! 😜🎂🎈 (walaupun telat harusnya kemarin wkwk)

    mode serius dulu wkwk
    """
    text1_html = text1.replace("\n", "<br>")
    st.markdown(f"<h2 style='text-align: justify; color: grey;font-size: 15px;'>{text1_html}</h2>", unsafe_allow_html=True)

    # Tombol kedua
    if st.button("Ini Beneran disini hadiahnyaaa 🚀🚀 ") or st.session_state.clicked_2:
        st.session_state.clicked_2 = True
        st.image("IMG_20240523_113306_205.jpg")
        text2 = """
        MAAF AKU NGAKAK SAMA FOTONYA WKWKKW
        
        """
        text2_html = text2.replace("\n", "<br>")
        st.markdown(f"<h2 style='text-align: center; color: grey;font-size: 30px;'>{text2_html}</h2>", unsafe_allow_html=True)
        
        # Tombol ketiga
        if st.button("Wkwkw Ini hadiahnya disini 😲 ") or st.session_state.clicked_3:
            st.session_state.clicked_3 = True
            st.image("IMG_20240524_065239_78522222.jpg")
            text3 = """
            Dan inilah kita, trio wek-wek yang selalu kompak, walaupun kadang-kadang lebih banyak ngakaknya daripada seriusnya. Semoga tetap berkabar apapun yang terjadi. 

            Tetap jaga kesehatan, jangan lupa makan sayur dan OLAHRAGA dan semoga kita semua sukses dalam segala hal yang kita lakukan. Oh ya, jangan sampai lupa, kita masih punya banyak petualangan seru yang menunggu! 🎉 (klo ada lagi wkwk)

            Ditunggu Traktiranyyaa luxxyyyy

     
            """
            text3_html = text3.replace("\n", "<br>")
            st.markdown(f"<h2 style='text-align: justify; color: grey;font-size: 15px;'>{text3_html}</h2>", unsafe_allow_html=True)
            if st.button("Terakhir") or st.session_state.clicked_4:
                st.session_state.clicked_4 = True
                st.markdown(f"<h2 style='text-align: center; color: black;font-size: 35px;'>SELAMAT BERTAMBAH TUA 👵</h2>", unsafe_allow_html=True)
                st.markdown("<h3 style='text-align: center;font-size: 25px;'>🎂 Happy 25 luxxxx! 🎂</h3>", unsafe_allow_html=True)
