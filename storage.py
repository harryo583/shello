import json
import os

STORAGE_FILE = "shello_data.json"

def save_bookmarks(bookmarks):
    data = {'bookmarks': bookmarks}
    with open(STORAGE_FILE, 'w') as f:
        json.dump(data, f)

def load_bookmarks():
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, 'r') as f:
        data = json.load(f)
    return data.get('bookmarks', [])
