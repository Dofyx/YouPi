#!/usr/bin/python3

# Flask
from flask import Flask, render_template, request, redirect
import subprocess
app = Flask(__name__)

# Telnet
import telnetlib, time
host = '127.0.0.1'
port = 5824
passwd = 'you314'

# API
@app.route('/')
def index():
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'playlist 1\n')
    time.sleep(1)
    output = tn.read_very_eager()
    tn.close()
    playlist = output.decode() + "\n"
    return render_template('index.html', html_playlist=playlist)

@app.route('/', methods=['POST'])
def add():
    link = request.form['youtube_link']
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'enqueue ' + str(link).encode('ascii') + b'\n')
    tn.close()
    return redirect("/")

@app.route('/play', methods=['POST'])
def play_api():
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'play\n')
    tn.close()
    return redirect("/")

@app.route('/stop', methods=['POST'])
def stop_api():
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'stop\n')
    tn.close()
    return redirect("/")

@app.route('/pause', methods=['POST'])
def pause_api():
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'pause\n')
    tn.close()
    return redirect("/")

@app.route('/next', methods=['POST'])
def next_api():
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'next\n')
    tn.close()
    return redirect("/")

@app.route('/prev', methods=['POST'])
def prev_api():
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'prev\n')
    tn.close()
    return redirect("/")

@app.route('/clear', methods=['POST'])
def clear_api():
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'clear\n')
    tn.close()
    return redirect("/")

@app.route('/volup', methods=['POST'])
def volup_api():
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'volup 1\n')
    tn.close()
    return redirect("/")

@app.route('/voldown', methods=['POST'])
def voldown_api():
    tn=telnetlib.Telnet(host, port)
    tn.read_until(b"Password: ")
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'voldown 1\n')
    tn.close()
    return redirect("/")

# run server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
