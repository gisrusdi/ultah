import streamlit as st
from streamlit.components.v1 import html
from urllib.parse import quote_plus
import time

# # Definisikan fungsi untuk pembersihan cache
# @st.experimental_memo
# def get_cache_cleared():
#     return True

# # Panggil fungsi untuk memaksa pembersihan cache
# get_cache_cleared()

# Pengaturan halaman
st.set_page_config(page_title="Ucapan Ulang Tahun", page_icon="🎉", layout="centered")


# Menambahkan musik latar belakang
audio_file = open("music.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3', start_time=25, autoplay=True)

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

  for (let i = 0; i < 100; i++) {
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
st.image("foto.png", caption="Happy Birthday!", use_column_width=True)

# Ucapan
st.markdown("<h2 style='text-align: center;'>Semoga hari ini penuh dengan kebahagiaan dan cinta. Selamat Ulang Tahun!</h2>", unsafe_allow_html=True)





# Putar video pendek
if st.button("Tekan ini untuk kejutan pertama!"):
    st.balloons()
    st.video("video.mp4")

# Menambahkan footer

# Harapan
st.write("**Tuliskan harapanmu di bawah ini:**")
user_wish = st.text_input("Harapan:")


# Jika pengguna sudah mengisi harapan
if user_wish:
    # Encode harapan untuk URL
    time.sleep(3)
    encoded_wish = quote_plus(user_wish)

    # Membuat link WhatsApp
    whatsapp_url = f"https://wa.me/6285728239628?text={encoded_wish}"
    
    # Menampilkan harapan dan balasan otomatis
    st.write(f"Harapanmu: {user_wish}")
    st.write("Aku pun berdoa itu akan menjadi kenyataan 🙏")

    # Menyisipkan HTML dan JavaScript untuk menunggu 5 detik dan membuka tab baru
    js_code = f"""
    <script>
    window.onload = function() {{
        var url = "{whatsapp_url}";
        window.open(url, "_blank");
    }}
    </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>🎂 Have a great day! 🎂</h3>", unsafe_allow_html=True)
