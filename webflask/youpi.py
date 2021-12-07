#!/usr/bin/python3

# Flask
from flask import Flask, render_template, request, redirect
import subprocess
app = Flask(__name__)

# Telnet
import telnetlib
host = '127.0.0.1'
port = 5824
passwd = 'you314'
def tnconnect():
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')

# API
@app.route('/')
def index():
    tnconnect()
    tn.write(b'playlist 1\n')
    output = tn.read_eager()
    playlist = output.decode() + "\n"
    tn.close()
    return render_template('index.html', html_playlist=playlist)

@app.route('/', methods=['POST'])
def add():
    link = request.form['youtube_link']
    tnconnect()
    tn.write(b'add ' + str(link).encode('ascii') + b'\n')
    tn.close()
    return redirect('/')
    
@app.route('/play', methods=['GET'])
def play_api():
    tnconnect()
    tn.write(b'play\n')
    tn.close()
    return redirect('/')

@app.route('/stop', methods=['GET'])
def stop_api():
    tnconnect()
    tn.write(b'stop\n')
    tn.close()
    return redirect('/')

@app.route('/pause', methods=['GET'])
def pause_api():
    tnconnect()
    tn.write(b'pause\n')
    tn.close()
    return redirect('/')

@app.route('/next', methods=['GET'])
def next_api():
    tnconnect()
    tn.write(b'next\n')
    tn.close()
    return redirect('/')

@app.route('/prev', methods=['GET'])
def prev_api():
    tnconnect()
    tn.write(b'prev\n')
    tn.close()
    return redirect('/')
    
@app.route('/volup', methods=['GET'])
def volup_api():
    tnconnect()
    tn.write(b'volup 1\n')
    tn.close()
    return redirect('/')
    
@app.route('/voldown', methods=['GET'])
def voldown_api():
    tnconnect()
    tn.write(b'voldown 1\n')
    tn.close()
    return redirect('/')

# run server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
