from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/play')
def play():
    subprocess.call(['./youpiPlay.sh'], shell=True) 
  
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
