    "Nhập văn bản cần dịch:",
    placeholder="Nhập vào đây (Ví dụ: Hello, Bonjour, Hola...)",
)

if st.button("Dịch sang Tiếng Việt", type="primary"):
    text = text_to_translate.strip()

    if not text:
        st.warning("Vui lòng nhập văn bản cần dịch!")
    elif len(text) > 5000:
        st.warning("Văn bản quá dài (tối đa 5000 ký tự). Hãy chia nhỏ ra nhé!")
    else:
        # Bước 1: Dịch
        translated_text = None
        try:
            with st.spinner("Đang dịch..."):
                translated_text = GoogleTranslator(source="auto", target="vi").translate(text)
        except Exception as e:
            st.error(f"Lỗi khi dịch: {e}")

        # Bước 2: Hiện kết quả, rồi mới đọc thành tiếng
        if translated_text:
            st.success("Kết quả dịch:")
            st.info(translated_text)

            try:
                audio_buffer = io.BytesIO()
                gTTS(text=translated_text, lang="vi").write_to_fp(audio_buffer)
                st.audio(audio_buffer.getvalue(), format="audio/mp3")
            except Exception as e:
                st.warning(f"Dịch thành công nhưng không tạo được âm thanh: {e}")
        elif translated_text is None:
            pass  # lỗi đã được hiển thị ở trên
        else:
            st.error("Không thể dịch được văn bản này. Bạn hãy thử lại nhé!")
