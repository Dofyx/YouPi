#!/usr/bin/python3

from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def play():
    link = request.form['youtube_link']
    youplay = 'cvlc --play-and-exit ' + link + ' > /dev/null 2>&1'
    subprocess.call(['pkill vlc'], shell=True)
    subprocess.call(youplay, shell=True)

@app.route('/play')
def play_api():
    id = request.args['id']
    link_api = 'https://www.youtube.com/watch?v=' + id
    youplay_api = 'cvlc --play-and-exit ' + link_api + ' > /dev/null 2>&1'
    subprocess.call(['pkill vlc'], shell=True)
    subprocess.call(youplay_api, shell=True)

@app.route('/stop')
def stop_api():
    subprocess.call(['pkill vlc'], shell=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
