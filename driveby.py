from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def get_file(filename):
    return send_file(f'payload.py')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
