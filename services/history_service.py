from datetime import datetime

# List to hold download history
download_history = []

def add_to_history(title, file_type):
    download_history.append({
        "title": title,
        "type": file_type,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

def get_download_history():
    return {"history": download_history}
