import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.set_page_config(page_title="App Dịch Ngôn Ngữ Thông Minh", page_icon="🇻🇳", layout="centered")

st.title("🌐 Ứng Dụng Dịch Ngôn Ngữ Thông Minh sang Tiếng Việt")
st.write("Nhập bất kỳ văn bản bằng ngôn ngữ nào, hệ thống sẽ tự động nhận diện và dịch sang tiếng Việt cho bạn.")

# Ô nhập văn bản
text_to_translate = st.text_area("Nhập văn bản cần dịch:", placeholder="Nhập vào đây (Ví dụ: Hello, Bonjour, Hola...)")

if st.button("Dịch sang Tiếng Việt", type="primary"):
    if text_to_translate.strip() != "":
        try:
            # Sử dụng GoogleTranslator với cơ chế tự động phát hiện ngôn ngữ nguồn (source='auto')
            translator = GoogleTranslator(source='auto', target='vi')
            translated_text = translator.translate(text_to_translate)
            
            st.success("### Kết quả dịch:")
            st.info(translated_text)
            
            # Tính năng đọc văn bản tiếng Việt
            tts = gTTS(text=translated_text, lang='vi')
            audio_file = "translated_audio.mp3"
            tts.save(audio_file)
            st.audio(audio_file, format='audio/mp3')
            
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {e}")
    else:
            st.warning("Vui lòng nhập văn bản cần dịch!")
