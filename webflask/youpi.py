#!/usr/bin/python3

# Flask
from flask import Flask, render_template, request, redirect
import subprocess
app = Flask(__name__)

# vlc instance
import pexpect
vlc = pexpect.spawn("vlc --no-video") #vlc instance to play the videos 
vlc.expect('>')

# API
@app.route('/')
def index():
    
    return render_template('index.html', html_playlist=playlist)

@app.route('/', methods=['POST'])
def add():
    link = request.form['youtube_link']
   
    return redirect("/")

@app.route('/play', methods=['POST'])
def play_api():
    
    return redirect("/")

@app.route('/stop', methods=['POST'])
def stop_api():
    
    return redirect("/")

@app.route('/pause', methods=['POST'])
def pause_api():
    
    return redirect("/")

@app.route('/next', methods=['POST'])
def next_api():
   
    return redirect("/")

@app.route('/prev', methods=['POST'])
def prev_api():
    
    return redirect("/")

@app.route('/clear', methods=['POST'])
def clear_api():
  
    return redirect("/")

@app.route('/volup', methods=['POST'])
def volup_api():
   
    return redirect("/")

@app.route('/voldown', methods=['POST'])
def voldown_api():
    
    return redirect("/")

# run server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
