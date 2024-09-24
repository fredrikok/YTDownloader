from flask import Flask, request, jsonify, send_file, send_from_directory # type: ignore
from flask_cors import CORS # type: ignore
from flask_swagger_ui import get_swaggerui_blueprint # type: ignore
import yt_dlp # type: ignore
import os

app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "YouTube Downloader API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/', methods=['GET'])
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/getapi', methods=['GET'])
def get_string():
    return jsonify({"message": "This is a simple string response."})

@app.route('/download', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        url = data.get('url')

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'best'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([url])

        info_dict = ydl.extract_info(url, download=False)
        file_path = os.path.join("downloads", f"{info_dict['title']}.mp4")

        return send_file(file_path, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
