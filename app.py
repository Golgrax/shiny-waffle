from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:path>')
def pages(path):
    # Check if the requested path corresponds to an HTML file in templates
    html_file = f"{path}.html"
    if os.path.exists(os.path.join(app.template_folder, html_file)):
        return render_template(html_file)
    
    # Otherwise, try serving from static
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
