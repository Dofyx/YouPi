#!/usr/bin/python3

from flask import Flask, render_template, request
import subprocess
import televlc

vlc = televlc.VLC(PASSWORD, 127.0.0.1, PORT)

vlc.connect_to_telnet_interface()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def add():
    link = request.form['youtube_link']
    command = 'add ' + link
    vlc.do(command)

@app.route('/play', methods=['GET'])
def play_api():
    command = 'play'
    vlc.do(command)

@app.route('/stop', methods=['GET'])
def stop_api():
    command = 'stop'
    vlc.do(command)

@app.route('/pause', methods=['GET'])
def pause_api():
    command = 'pause'
    vlc.do(command)
    
@app.route('/volup', methods=['GET'])
def volup_api():
    command = ["volup", "1"]
    vlc.do(command)
    
@app.route('/voldown', methods=['GET'])
def voldown_api():
    command = ["voldown", "1"]
    vlc.do(command)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
