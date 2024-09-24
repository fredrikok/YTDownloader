import yt_dlp
import os
from datetime import datetime
from flask import jsonify
from services.history_service import add_to_history

DOWNLOADS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../downloads')

def download_video_service(request):
    try:
        data = request.get_json()
        url = data.get('url')

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOADS_DIR, '%(title)s.%(ext)s'),
            'format': 'best'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        info_dict = ydl.extract_info(url, download=False)
        file_url = f"/download_file/{info_dict['title']}.mp4"
        add_to_history(info_dict['title'], 'mp4')

        return jsonify({"file_url": file_url})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def download_mp3_service(request):
    try:
        data = request.get_json()
        url = data.get('url')

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(DOWNLOADS_DIR, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        info_dict = ydl.extract_info(url, download=False)
        file_url = f"/download_file/{info_dict['title']}.mp3"
        add_to_history(info_dict['title'], 'mp3')

        return jsonify({"file_url": file_url})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
