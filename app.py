import streamlit as st
import datetime

# Настройка страницы браузера
st.set_page_config(
    page_title="Для моей дорогой девочки",
    page_icon="💙",
    layout="centered"
)

# Внедрение стилей оформления (Черный + Голубой неон)
st.markdown("""
    <style>
        .stApp {
            background-color: #0b0f19;
            font-family: 'Georgia', serif;
        }
        .main-card {
            background: #161b26;
            border: 2px solid rgba(0, 180, 216, 0.3);
            border-radius: 20px;
            padding: 40px 25px;
            text-align: center;
            box-shadow: 0 0 30px rgba(0, 180, 216, 0.15);
            color: #f8f9fa;
            margin-top: 20px;
        }
        .card-title {
            font-size: 26px;
            color: #f8f9fa;
            line-height: 1.5;
            text-shadow: 0 0 10px rgba(0, 180, 216, 0.4);
            margin-bottom: 20px;
            font-style: italic;
        }
        .envelope {
            font-size: 60px;
            margin: 20px 0;
            filter: drop-shadow(0 0 15px rgba(0, 180, 216, 0.5));
        }
        .timer-box {
            background: rgba(11, 15, 25, 0.6);
            border: 1px solid rgba(0, 180, 216, 0.2);
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 25px;
        }
        .timer-title {
            font-size: 13px;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .timer-digits {
            font-size: 24px;
            color: #00b4d8;
            font-family: 'Consolas', monospace;
            font-weight: bold;
            text-shadow: 0 0 8px #3a86ff;
        }
        .letter-text {
            font-size: 16px;
            line-height: 1.9;
            color: #e2e8f0;
            text-align: justify;
            text-indent: 20px;
            margin-bottom: 20px;
        }
        .letter-heart {
            font-size: 18px;
            color: #00b4d8;
            font-weight: bold;
            text-shadow: 0 0 8px #3a86ff;
            margin-top: 25px;
        }
        .hint-text {
            color: #64748b;
            font-size: 12px;
            font-style: italic;
            margin-top: 5px;
            margin-bottom: 15px;
            text-align: center;
        }
        /* Стилизация кнопок */
        div.stButton > button {
            background-color: rgba(0, 180, 216, 0.1) !important;
            color: #f8f9fa !important;
            border: 2px solid #00b4d8 !important;
            border-radius: 25px !important;
            padding: 10px 25px !important;
            font-family: 'Segoe UI', serif !important;
            font-weight: bold !important;
            letter-spacing: 1px !important;
            text-transform: uppercase !important;
            transition: all 0.3s ease !important;
        }
        div.stButton > button:hover {
            background-color: #00b4d8 !important;
            color: #0b0f19 !important;
            box-shadow: 0 0 25px #3a86ff !important;
        }
        /* Стилизация поля ввода */
        div.stTextInput input {
            background-color: #0b0f19 !important;
            color: #f8f9fa !important;
            border: 1px solid #1e3d59 !important;
            text-align: center !important;
            font-size: 16px !important;
        }
        div.stTextInput input:focus {
            border-color: #00b4d8 !important;
            box-shadow: 0 0 10px rgba(0, 180, 216, 0.5) !important;
        }
    </style>
""", unsafe_allow_html=True)

# Инициализация состояния
if 'opened' not in st.session_state:
    st.session_state.opened = False
if 'error_msg' not in st.session_state:
    st.session_state.error_msg = ""

# РЕНДЕРИНГ ИНТЕРФЕЙСА
if not st.session_state.opened:
    # ОБЛОЖКА
    st.markdown("""
        <div class="main-card">
            <div class="card-title">Моей любимой девочке<br>в нашу дату ✨</div>
            <div class="envelope">💙✉️🖤</div>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    code = st.text_input("Введи секретное кодовое слово:", type="password", key="secret_code_input")
    st.markdown('<div class="hint-text">Подсказка: вспомни, что мы говорим перед тем, как сказать мяу... 🐾</div>',
                unsafe_allow_html=True)

    if st.session_state.error_msg:
        st.error(st.session_state.error_msg)

    # Исправлено: передаем число 3 в columns
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Нажми, чтобы открыть", use_container_width=True):
            if code.strip().lower() == "бурмалда":
                st.session_state.opened = True
                st.session_state.error_msg = ""
                st.rerun()
            else:
                st.session_state.error_msg = "Неверное кодовое слово! Попробуй еще раз 🤫"
                st.rerun()
else:
    # ВНУТРЕННЯЯ СТОРОНА (ПИСЬМО)
    st.snow()  # Теперь снежинки падают плавно и непрерывно!

    # HTML/JS Скрипт живого таймера, который плавно идет на самом устройстве
    # Начало: 3 мая 2026 года
    timer_html = """
    <div class="timer-box" style="background: rgba(11, 15, 25, 0.6); border: 1px solid rgba(0, 180, 216, 0.2); border-radius: 12px; padding: 15px; margin-bottom: 25px; text-align: center;">
        <div class="timer-title" style="font-size: 13px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; font-weight: bold; font-family: 'Segoe UI', sans-serif;">Мы вместе уже:</div>
        <div id="live-timer" class="timer-digits" style="font-size: 24px; color: #00b4d8; font-family: 'Consolas', monospace; font-weight: bold; text-shadow: 0 0 8px #3a86ff;">Загрузка таймера...</div>
    </div>

    <script>
        const startDate = new Date('2026-05-03T00:00:00');

        function updateTimer() {
            const now = new Date();
            const difference = now - startDate;

            if (difference < 0) {
                document.getElementById('live-timer').innerText = "0д 00:00:00";
                return;
            }

            const days = Math.floor(difference / (1000 * 60 * 60 * 24));
            const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((difference % (1000 * 60)) / 1000);

            const fHours = hours.toString().padStart(2, '0');
            const fMinutes = minutes.toString().padStart(2, '0');
            const fSeconds = seconds.toString().padStart(2, '0');

            document.getElementById('live-timer').innerText = `${days}д ${fHours}:${fMinutes}:${fSeconds}`;
        }

        setInterval(updateTimer, 1000);
        updateTimer();
    </script>
    """

    # Отрендерить таймер и текст письма
    st.components.v1.html(timer_html, height=100)

    st.markdown("""
        <div class="main-card" style="background: #1f2633; margin-top: 0px;">
            <div class="letter-text">
                Моя дорогая девочка, я очень сильно тебя люблю. Я безумно рад быть с тобой и наслаждаться твоим присутствием в моей жизни. Каждый день я благодарен за то, что ты есть у меня.
            </div>
            <div class="letter-text">
                Меня до сих пор забавляет и удивляет, что по такой чистой случайности мы вообще познакомились и вот мы уже так долго вместе!
            </div>
            <div class="letter-text">
                За эти полгода мы столько пережили прекрасных моментов. Да, бывали иногда и немного плохие моменты, но они абсолютно не сравнятся с хорошими. Ты — моё солнце, и никакие расстояния этого не изменят.
            </div>
            <div class="letter-heart">я очень люблю тебя моя дорогая 🖤</div>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    # Исправлено: передаем число 3 в columns
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Закрыть письмо", use_container_width=True):
            st.session_state.opened = False
            st.rerun()
