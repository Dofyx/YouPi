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
    add_cmd = "enqueue " + link
    vlc.sendline(add_cmd)
    vlc.expect('>')
    return redirect("/")

@app.route('/play')
def play_api():
    vlc.sendline("play")
    vlc.expect('>')
    return redirect("/")

@app.route('/stop')
def stop_api():
    vlc.sendline("stop")
    vlc.expect('>')
    return redirect("/")

@app.route('/pause')
def pause_api():
    vlc.sendline("pause")
    vlc.expect('>')
    return redirect("/")

@app.route('/next')
def next_api():
    vlc.sendline("next")
    vlc.expect('>')
    return redirect("/")

@app.route('/prev')
def prev_api():
    vlc.sendline("prev")
    vlc.expect('>')
    return redirect("/")

@app.route('/clear')
def clear_api():
    vlc.sendline("clear")
    vlc.expect('>')
    return redirect("/")

@app.route('/volup')
def volup_api():
    vlc.sendline("volup 1")
    vlc.expect('>')
    return redirect("/")

@app.route('/voldown')
def voldown_api():
    vlc.sendline("voldown 1")
    vlc.expect('>')
    return redirect("/")

# run server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
