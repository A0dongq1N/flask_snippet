import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(10)
    return 'Hello, World!'


if __name__ == '__main__':
    # gunicorn -w 4 -b 127.0.0.1:8000 --timeout 5 gunicorn_snippet:app
    app.run(debug=False)