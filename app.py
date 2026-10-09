import streamlit as st
from googletrans import Translator
from gtts import gTTS

st.set_page_config(page_title="App Dịch Ngôn Ngữ Thông Minh", page_icon="🇻🇳", layout="centered")

st.title("🌐 Ứng Dụng Dịch Ngôn Ngữ Thông Minh sang Tiếng Việt")
st.write("Nhập bất kỳ văn bản bằng ngôn ngữ nào, hệ thống sẽ tự động nhận diện và dịch sang tiếng Việt cho bạn.")

# Khởi tạo translator
translator = Translator()

# Ô nhập văn bản
text_to_translate = st.text_area("Nhập văn bản cần dịch:", placeholder="Nhập vào đây (Ví dụ: Hello, Bonjour, Hola...)")

if st.button("Dịch sang Tiếng Việt", type="primary"):
    if text_to_translate.strip() != "":
        try:
            # Tự động dịch sang tiếng Việt (dest='vi')
            translation = translator.translate(text_to_translate, dest='vi')
            
            st.success("### Kết quả dịch:")
            st.info(translation.text)
            
            # Tính năng đọc văn bản tiếng Việt
            tts = gTTS(text=translation.text, lang='vi')
            audio_file = "translated_audio.mp3"
            tts.save(audio_file)
            st.audio(audio_file, format='audio/mp3')
            
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {e}. Bạn hãy thử lại nhé!")
    else:
        st.warning("Vui lòng nhập văn bản cần dịch!")
