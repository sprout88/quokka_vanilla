from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def get_file():
    return send_file('server.py')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
