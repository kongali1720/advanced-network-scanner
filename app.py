from flask import Flask, render_template, request
from advanced_scanner import run_scan  # kita akan gunakan fungsi scanning dari script asli

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        host = request.form['host']
        start_port = int(request.form['start_port'])
        end_port = int(request.form['end_port'])
        results = run_scan(host, start_port, end_port)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
