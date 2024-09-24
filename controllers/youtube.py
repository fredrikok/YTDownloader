from flask import Blueprint, request, jsonify, send_from_directory
from services.download_service import download_video_service, download_mp3_service
from services.history_service import get_download_history

youtube_blueprint = Blueprint('youtube', __name__)

# Serve YouTube MP4 downloader page
@youtube_blueprint.route('/youtube/ytmp4', methods=['GET'])
def serve_ytmp4_page():
    return send_from_directory('static/Youtube', 'ytmp4.html')

# Serve YouTube MP3 downloader page
@youtube_blueprint.route('/youtube/ytmp3', methods=['GET'])
def serve_ytmp3_page():
    return send_from_directory('static/Youtube', 'ytmp3.html')

# Download video and return download link (MP4)
@youtube_blueprint.route('/download', methods=['POST'])
def download_video():
    return download_video_service(request)

# Download MP3 and return download link
@youtube_blueprint.route('/download_mp3', methods=['POST'])
def download_mp3():
    return download_mp3_service(request)

# Serve the downloaded file
@youtube_blueprint.route('/download_file/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('downloads', filename, as_attachment=True)

# Get download history
@youtube_blueprint.route('/history', methods=['GET'])
def download_history():
    return jsonify(get_download_history())
