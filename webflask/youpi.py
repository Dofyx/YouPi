from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form_post():
    link = request.form['youtube_link']
    subprocess.call(['pkill vlc'], shell=True)
    subprocess.call(['./youpiPlay.sh', link], shell=True)
    return render_template('index.html')

@app.route('/play')
def play():
    id = request.args['id']
    link1 = 'https://www.youtube.com/watch?v=' + id
    subprocess.call(['pkill vlc'], shell=True)
    subprocess.call(['./youpiPlay.sh', link1], shell=True)
    return render_template('index.html')

@app.route('/stop')
def stop():
    subprocess.call(['pkill vlc'], shell=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
