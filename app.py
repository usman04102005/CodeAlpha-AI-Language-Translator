from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)

translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/translate', methods=['POST'])
def translate_text():

    try:
        data = request.json

        text = data.get('text', '')
        source_lang = data.get('source_lang', 'auto')
        target_lang = data.get('target_lang', 'en')

        if not text:
            return jsonify({
                'error': 'No text provided'
            }), 400

        translated = translator.translate(
            text,
            src=source_lang,
            dest=target_lang
        )

        return jsonify({
            'original': text,
            'translated': translated.text,
            'source_lang': source_lang,
            'target_lang': target_lang
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/languages', methods=['GET'])
def get_languages():

    languages = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'pt': 'Portuguese',
        'ru': 'Russian',
        'ja': 'Japanese',
        'zh-CN': 'Chinese (Simplified)',
        'ar': 'Arabic',
        'hi': 'Hindi',
        'ur': 'Urdu',
        'auto': 'Auto-detect'
    }

    return jsonify(languages)


if __name__ == '__main__':
    app.run(debug=True, port=5000)