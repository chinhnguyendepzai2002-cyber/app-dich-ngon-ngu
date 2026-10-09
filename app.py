import io
import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

st.set_page_config(page_title="App Dịch Ngôn Ngữ Thông Minh", page_icon="🇻🇳", layout="centered")

st.title("🌐 Ứng Dụng Dịch Ngôn Ngữ Thông Minh sang Tiếng Việt")
st.write("Nhập bất kỳ văn bản bằng ngôn ngữ nào, hệ thống sẽ tự động nhận diện và dịch sang tiếng Việt cho bạn.")

text_to_translate = st.text_area("Nhập văn bản cần dịch:", placeholder="Ví dụ: Hello, Bonjour, Hola...")

if st.button("Dịch sang Tiếng Việt", type="primary"):
    text = text_to_translate.strip()
    if not text:
        st.warning("Vui lòng nhập văn bản cần dịch!")
    else:
        translated_text = None
        try:
            translated_text = GoogleTranslator(source="auto", target="vi").translate(text)
        except Exception as e:
            st.error(f"Lỗi khi dịch: {e}")

        if translated_text:
            st.success("Kết quả dịch:")
            st.info(translated_text)
            try:
                buf = io.BytesIO()
                gTTS(text=translated_text, lang="vi").write_to_fp(buf)
                st.audio(buf.getvalue(), format="audio/mp3")
            except Exception as e:
                st.warning(f"Không tạo được âm thanh: {e}")
