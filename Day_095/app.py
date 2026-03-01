import os
import base64
from flask import Flask, render_template, request, jsonify
from gtts import gTTS
from io import BytesIO
import PyPDF2

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    try:
        pdf_reader = PyPDF2.PdfReader(file)
        full_text_blocks = []
        for i, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            if page_text:
                full_text_blocks.append(page_text)
                full_text_blocks.append(f" End of page {i + 1}. ")

        if not full_text_blocks:
            raise ValueError("Could not extract any text from this PDF.")
        final_script = "".join(full_text_blocks)

        # We process the first 5000 chars to keep it snappy for the browser
        tts = gTTS(text=final_script[:5000], lang='en', slow=False)

        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        audio_base64 = base64.b64encode(audio_fp.read()).decode('utf-8')

        return jsonify({
            "status": "success",
            "audio_base64": audio_base64,
            "filename": file.filename.replace(".pdf", ".mp3")
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)