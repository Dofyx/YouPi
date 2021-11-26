from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    link = request.form['youtube_link']
    subprocess.call(["./youpiPlay.sh", link], shell=True)
    return render_template('index.html')

@app.route('/play')
def play():
    subprocess.call(['./youpiPlay.sh'], shell=True)
    return render_template('index.html')

@app.route('/stop')
def stop():
    subprocess.call(['./youpiStop.sh'], shell=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
