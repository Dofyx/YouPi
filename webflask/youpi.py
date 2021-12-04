#!/usr/bin/python3

from flask import Flask, render_template, request
import subprocess
import televlc

vlc = televlc.VLC(you314, 127.0.0.1, 5824)

vlc.connect_to_telnet_interface()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def add():
    link = request.form['youtube_link']
    command_add = 'add ' + link
    vlc.do(command_add)

@app.route('/play', methods=['GET'])
def play_api():
    command_play = 'play'
    vlc.do(command_play)

@app.route('/stop', methods=['GET'])
def stop_api():
    command_stop = 'stop'
    vlc.do(command_stop)

@app.route('/pause', methods=['GET'])
def pause_api():
    command_pause = 'pause'
    vlc.do(command_pause)
    
@app.route('/volup', methods=['GET'])
def volup_api():
    command_volup = ["volup", "1"]
    vlc.do(command_volup)
    
@app.route('/voldown', methods=['GET'])
def voldown_api():
    command_voldown = ["voldown", "1"]
    vlc.do(command_voldown)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
