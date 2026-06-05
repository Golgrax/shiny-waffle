from flask import Flask, send_from_directory
import os
from templates import index, about, contact, projects, skills, page_not_found, error_404

app = Flask(__name__, static_folder='static')

PAGES = {
    'index': index.content,
    'about': about.content,
    'contact': contact.content,
    'projects': projects.content,
    'skills': skills.content,
    '404': error_404.content,
    '_not-found': page_not_found.content
}

@app.route('/')
def home():
    return PAGES['index']

@app.route('/<path:path>')
def serve_pages(path):
    # Check if path is in our PAGES mapping
    if path in PAGES:
        return PAGES[path]
    
    # Check if it's a file in static
    static_file = os.path.join(app.static_folder, path)
    if os.path.isfile(static_file):
        return send_from_directory(app.static_folder, path)
    
    # Fallback to 404
    return PAGES['404'], 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
