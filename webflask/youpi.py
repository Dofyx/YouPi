#!/usr/bin/python3

# Flask
from flask import Flask, render_template, request, redirect, Response
import subprocess
app = Flask(__name__)

# vlc instance
import pexpect
vlc = pexpect.spawn("vlc --novideo")
vlc.expect('>')

# API
@app.route('/')
def index():
    
    return render_template('index.html', html_playlist=playlist)

@app.route('/', methods=['POST'])
def add():
    link = request.form['youtube_link']
    add_cmd = "enqueue " + link # sends this command to the vlc instance 
    vlc.sendline(add_cmd)
    vlc.expect('>')
    return redirect("/")

@app.route('/play', methods=['POST'])
def play_api():
    vlc.sendline("play")
    vlc.expect('>')
    return redirect("/")

@app.route('/stop', methods=['POST'])
def stop_api():
    vlc.sendline("stop")
    vlc.expect('>')
    return redirect("/")

@app.route('/pause', methods=['POST'])
def pause_api():
    vlc.sendline("pause")
    vlc.expect('>')
    return redirect("/")

@app.route('/next', methods=['POST'])
def next_api():
    vlc.sendline("next")
    vlc.expect('>')
    return redirect("/")

@app.route('/prev', methods=['POST'])
def prev_api():
    vlc.sendline("prev")
    vlc.expect('>')
    return redirect("/")

@app.route('/clear', methods=['POST'])
def clear_api():
    vlc.sendline("clear")
    vlc.expect('>')
    return redirect("/")

@app.route('/volup', methods=['POST'])
def volup_api():
    vlc.sendline("volup 1")
    vlc.expect('>')
    return redirect("/")

@app.route('/voldown', methods=['POST'])
def voldown_api():
    vlc.sendline("voldown 1")
    vlc.expect('>')
    return redirect("/")

# run server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
