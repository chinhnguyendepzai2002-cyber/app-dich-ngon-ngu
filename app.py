import streamlit as st
from gtts import gTTS
import urllib.request
import urllib.parse
import json

st.set_page_config(page_title="App Dịch Ngôn Ngữ Thông Minh", page_icon="🇻🇳", layout="centered")

st.title("🌐 Ứng Dụng Dịch Ngôn Ngữ Thông Minh sang Tiếng Việt")
st.write("Nhập bất kỳ văn bản bằng ngôn ngữ nào, hệ thống sẽ tự động nhận diện và dịch sang tiếng Việt cho bạn.")

def translate_text(text):
    try:
        # Sử dụng API dịch thuật công khai trực tiếp
        encoded_text = urllib.parse.quote(text)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=vi&dt=t&q={encoded_text}"
        
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            # Ghép lại các đoạn được dịch
            translated_sentence = "".join([item[0] for item in res[0]])
            return translated_sentence
    except Exception as e:
        return None

# Ô nhập văn bản
text_to_translate = st.text_area("Nhập văn bản cần dịch:", placeholder="Nhập vào đây (Ví dụ: Hello, Bonjour, Hola...)")

if st.button("Dịch sang Tiếng Việt", type="primary"):
    if text_to_translate.strip() != "":
        translated_text = translate_text(text_to_translate)
        
        if translated_text:
            st.success("### Kết quả dịch:")
            st.info(translated_text)
            
            # Tính năng đọc văn bản tiếng Việt
            tts = gTTS(text=translated_text, lang='vi')
            audio_file = "translated_audio.mp3"
            tts.save(audio_file)
            st.audio(audio_file, format='audio/mp3')
        else:
            st.error("Đã xảy ra lỗi khi kết nối tới dịch vụ dịch thuật. Bạn hãy thử lại nhé!")
    else:
        st.warning("Vui lòng nhập văn bản cần dịch!")
