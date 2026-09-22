

import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(
    page_title="A Special Birthday",
    layout="wide"
)

# -----------------------------
# FILE PATHS
# -----------------------------

BASE_DIR = Path(__file__).parent

image1 = BASE_DIR / "images" / "photo1.jpeg"
image2 = BASE_DIR / "images" / "photo2.jpeg"
image3 = BASE_DIR / "images" / "photo3.jpeg"

music_file = BASE_DIR / "music" / "birthday.mp3"


# -----------------------------
# CONVERT FILES TO BASE64
# -----------------------------

def image_to_base64(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode()


def audio_to_base64(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode()


img1 = image_to_base64(image1)
img2 = image_to_base64(image2)
img3 = image_to_base64(image3)

music = audio_to_base64(music_file)


# -----------------------------
# HTML
# -----------------------------

page = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Serif+Display&display=swap" rel="stylesheet">

<style>

* {{
    box-sizing: border-box;
}}

html {{
    scroll-behavior: smooth;
}}

body {{
    margin: 0;
    padding: 0;
    background: #F6F0E5;
    color: #46513F;
    font-family: 'Cormorant Garamond', serif;
}}

button {{
    font-family: 'Cormorant Garamond', serif;
}}


/* =========================
   OPENING SCREEN
========================= */

.opening {{
    height: 650px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(circle at 15% 20%, rgba(199,169,107,0.12), transparent 25%),
        radial-gradient(circle at 85% 80%, rgba(138,154,123,0.13), transparent 28%),
        #F6F0E5;
}}

.circle {{
    position: absolute;
    border: 1px solid rgba(199,169,107,0.3);
    border-radius: 50%;
}}

.circle.one {{
    width: 300px;
    height: 300px;
    top: -130px;
    left: -100px;
}}

.circle.two {{
    width: 400px;
    height: 400px;
    bottom: -200px;
    right: -150px;
}}

.open-content {{
    position: relative;
    z-index: 2;
}}

.eyebrow {{
    font-size: 15px;
    letter-spacing: 7px;
    text-transform: uppercase;
    color: #8A8174;
}}

.gold-line {{
    width: 75px;
    height: 1px;
    background: #C7A96B;
    margin: 22px auto;
}}

.open-title {{
    font-family: 'DM Serif Display', serif;
    font-size: 58px;
    font-weight: 400;
    color: #3F4A3C;
    margin: 0;
}}

.open-subtitle {{
    font-size: 24px;
    color: #81786B;
    font-style: italic;
    margin-top: 12px;
}}

/* NEW: BIRTHDAY DATE */

.birthday-date {{
    font-family: 'DM Serif Display', serif;
    font-size: 34px;
    letter-spacing: 6px;
    color: #B08D4F;
    margin: 18px 0 5px;
}}

.date-year {{
    font-family: 'Cormorant Garamond', serif;
    font-size: 17px;
    letter-spacing: 4px;
    color: #8A8174;
    margin-top: 2px;
}}

.gift {{
    font-size: 65px;
    margin: 30px 0 25px;
    animation: floating 2.5s ease-in-out infinite;
}}

@keyframes floating {{
    0%,100% {{
        transform: translateY(0);
    }}

    50% {{
        transform: translateY(-10px);
    }}
}}

.open-button {{
    border: 1px solid #C7A96B;
    background: rgba(255,255,255,0.55);
    color: #46513F;
    padding: 14px 40px;
    font-size: 18px;
    letter-spacing: 3px;
    cursor: pointer;
    transition: 0.35s;
}}

.open-button:hover {{
    background: #46513F;
    color: white;
    transform: translateY(-3px);
}}

.open-note {{
    margin-top: 25px;
    font-size: 14px;
    color: #9A9184;
    letter-spacing: 1px;
}}


/* =========================
   MAIN BIRTHDAY
========================= */

#birthday {{
    display: none;
}}

.hero {{
    min-height: 650px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 70px 20px;
    background: #F6F0E5;
}}

.hero-small {{
    font-size: 15px;
    letter-spacing: 7px;
    color: #8A8174;
}}

.hero-title {{
    font-family: 'DM Serif Display', serif;
    font-size: 72px;
    font-weight: 400;
    letter-spacing: 5px;
    color: #46513F;
    margin: 20px 0 0;
}}

.hero-name {{
    font-family: 'DM Serif Display', serif;
    font-size: 82px;
    color: #B08D4F;
    margin: 5px 0 20px;
}}

.hero-text {{
    max-width: 650px;
    margin: auto;
    font-size: 23px;
    line-height: 1.6;
    color: #70685C;
}}

.decor {{
    font-size: 25px;
    color: #C7A96B;
    margin-top: 25px;
}}


/* =========================
   MUSIC BUTTON
========================= */

.music-button {{
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 100;
    border: 1px solid #C7A96B;
    background: rgba(255,253,247,0.92);
    color: #46513F;
    padding: 10px 18px;
    border-radius: 30px;
    cursor: pointer;
    font-size: 15px;
}}


/* =========================
   PHOTO SECTIONS
========================= */

.memory-section {{
    padding: 90px 25px;
    background: #FFFDF7;
    text-align: center;
}}

.memory-label {{
    font-size: 14px;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: #9A9184;
    margin-bottom: 20px;
}}

.photo-card {{
    max-width: 720px;
    margin: 0 auto;
}}

.photo-frame {{
    padding: 12px;
    background: #F6F0E5;
    border: 1px solid rgba(199,169,107,0.5);
    box-shadow: 0 20px 50px rgba(63,74,60,0.10);
}}

.photo-frame img {{
    display: block;
    width: 100%;
    height: auto;
}}

.photo-caption {{
    font-family: 'DM Serif Display', serif;
    font-size: 30px;
    color: #46513F;
    margin: 30px 0 12px;
}}

.photo-message {{
    max-width: 650px;
    margin: auto;
    font-size: 20px;
    line-height: 1.7;
    color: #756D61;
}}


/* =========================
   DUA SECTION
========================= */

.dua-section {{
    padding: 100px 25px;
    text-align: center;
    background: #E9E8DD;
}}

.dua-icon {{
    font-size: 35px;
    margin-bottom: 20px;
}}

.dua-title {{
    font-family: 'DM Serif Display', serif;
    font-size: 42px;
    color: #46513F;
    margin-bottom: 25px;
}}

.dua-text {{
    max-width: 760px;
    margin: auto;
    font-size: 23px;
    line-height: 1.8;
    color: #5F6255;
}}


/* =========================
   FINAL MESSAGE
========================= */

.final-section {{
    min-height: 600px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 70px 25px;
    background: #46513F;
    color: #F6F0E5;
}}

.final-content {{
    max-width: 800px;
}}

.final-small {{
    font-size: 15px;
    letter-spacing: 6px;
    color: #D9C99D;
}}

.final-title {{
    font-family: 'DM Serif Display', serif;
    font-size: 65px;
    font-weight: 400;
    margin: 25px 0 5px;
}}

.final-name {{
    font-family: 'DM Serif Display', serif;
    font-size: 72px;
    color: #D4B66F;
}}

.final-message {{
    font-size: 23px;
    line-height: 1.7;
    margin-top: 25px;
    color: #EEE8D8;
}}

.signature {{
    margin-top: 45px;
    font-size: 21px;
    font-style: italic;
    color: #D9C99D;
}}

.footer {{
    margin-top: 30px;
    font-size: 28px;
}}


/* =========================
   RESPONSIVE
========================= */

@media (max-width: 700px) {{

    .open-title {{
        font-size: 42px;
    }}

    .hero-title {{
        font-size: 48px;
    }}

    .hero-name {{
        font-size: 55px;
    }}

    .final-title {{
        font-size: 45px;
    }}

    .final-name {{
        font-size: 55px;
    }}

}}

</style>

</head>


<body>


<!-- =========================
     OPENING
========================= -->

<section class="opening" id="opening">

    <div class="circle one"></div>
    <div class="circle two"></div>

    <div class="open-content">

        <div class="eyebrow">
            A LITTLE SURPRISE
        </div>

        <div class="gold-line"></div>

        <h1 class="open-title">
            Something Special
        </h1>

        <div class="open-subtitle">
            is waiting for you...
        </div>

        <!-- NEW: BIRTHDAY DATE -->

        <div class="birthday-date">
            24 SEPTEMBER
        </div>

        <div class="date-year">
            2026
        </div>

        <div class="gift">
            🎁
        </div>

        <button class="open-button" onclick="openGift()">
            OPEN YOUR GIFT ✨
        </button>

        <div class="open-note">
            A little moment made especially for you
        </div>

    </div>

</section>


<!-- =========================
     MUSIC
========================= -->

<audio id="birthdayMusic" loop>
    <source src="data:audio/mpeg;base64,{music}" type="audio/mpeg">
</audio>

<button class="music-button" id="musicButton" onclick="toggleMusic()" style="display:none;">
    🎵 Music On
</button>


<!-- =========================
     BIRTHDAY EXPERIENCE
========================= -->

<div id="birthday">


<!-- HERO -->

<section class="hero">

    <div>

        <div class="hero-small">
            TODAY IS YOUR SPECIAL DAY
        </div>

        <!-- NEW: BIRTHDAY DATE -->

        <div class="birthday-date">
            24 SEPTEMBER
        </div>

        <div class="date-year">
            2026
        </div>

        <div class="gold-line"></div>

        <h1 class="hero-title">
            HAPPY BIRTHDAY
        </h1>

        <div class="hero-name">
            Abdul Hadi
        </div>

        <div class="hero-text">
            Today is a beautiful reminder of how special
            one person can be. May your new year of life
            bring you countless reasons to smile.
        </div>

        <div class="decor">
            ✦ &nbsp; ✦ &nbsp; ✦
        </div>

    </div>

</section>


<!-- PHOTO 1 -->

<section class="memory-section">

    <div class="memory-label">
        A BEAUTIFUL MOMENT
    </div>

    <div class="photo-card">

        <div class="photo-frame">
            <img src="data:image/jpeg;base64,{img1}">
        </div>

        <div class="photo-caption">
            Keep Smiling ❤️
        </div>

        <div class="photo-message">
            Your smile has a beautiful way of making
            ordinary moments feel special. May you
            always have a reason to smile from your heart.
        </div>

    </div>

</section>


<!-- PHOTO 2 -->

<section class="memory-section">

    <div class="memory-label">
        A SPECIAL MEMORY
    </div>

    <div class="photo-card">

        <div class="photo-frame">
            <img src="data:image/jpeg;base64,{img2}">
        </div>

        <div class="photo-caption">
            Always Believe In Yourself ✨
        </div>

        <div class="photo-message">
            Keep moving forward, keep learning and
            keep believing in yourself. May every step
            you take lead you towards something beautiful.
        </div>

    </div>

</section>


<!-- PHOTO 3 -->

<section class="memory-section">

    <div class="memory-label">
        ONE MORE BEAUTIFUL MOMENT
    </div>

    <div class="photo-card">

        <div class="photo-frame">
            <img src="data:image/jpeg;base64,{img3}">
        </div>

        <div class="photo-caption">
            You Are Very Special ❤️
        </div>

        <div class="photo-message">
            Never forget how special you are.
            May your life always be surrounded by
            happiness, love, peace and beautiful people.
        </div>

    </div>

</section>


<!-- DUA -->

<section class="dua-section">

    <div class="dua-icon">
        🤲
    </div>

    <div class="dua-title">
        A Special Dua For You
    </div>

    <div class="dua-text">
        May Allah always keep you happy, healthy and safe.
        May He bless you with success in every good thing
        you pursue, protect you from every difficulty,
        and fill your life with peace, happiness and countless
        beautiful moments. Ameen.
    </div>

</section>


<!-- FINAL -->

<section class="final-section">

    <div class="final-content">

        <div class="final-small">
            WITH ALL THE WARMEST WISHES
        </div>

        <div class="gold-line"></div>

        <div class="final-title">
            Happy Birthday
        </div>

        <div class="final-name">
            Abdul Hadi
        </div>

        <div class="final-message">
            May this new chapter of your life be filled
            with dreams that come true, moments worth
            remembering and happiness that never fades.
            Keep shining and keep being you. ❤️
        </div>

        <div class="signature">
            With warmest wishes,<br>
            Sundas Waqas
        </div>

        <div class="footer">
            ✦ 🤍 ✦
        </div>

    </div>

</section>


</div>


<script>

function openGift() {{

    const opening = document.getElementById("opening");
    const birthday = document.getElementById("birthday");
    const music = document.getElementById("birthdayMusic");
    const musicButton = document.getElementById("musicButton");

    opening.style.display = "none";

    birthday.style.display = "block";

    musicButton.style.display = "block";

    music.play().catch(function(error) {{
        console.log("Music could not autoplay:", error);
    }});

    window.scrollTo(0, 0);
}}


function toggleMusic() {{

    const music = document.getElementById("birthdayMusic");
    const button = document.getElementById("musicButton");

    if (music.paused) {{

        music.play();

        button.innerHTML = "🎵 Music On";

    }} else {{

        music.pause();

        button.innerHTML = "🔇 Music Off";

    }}

}}

</script>


</body>

</html>
"""

components.html(
    page,
    height=6000,
    scrolling=True
)
