import time
from flask import Flask, request

app = Flask(__name__)

@app.route('/http11')
def http11():
    # 获取协议版本
    protocol_version = request.environ.get('SERVER_PROTOCOL', '')
    print(f"protocol_version={protocol_version}")

    # 判断协议版本
    if 'HTTP/1.1' in protocol_version:
        version = 'HTTP/1.1'
    elif 'HTTP/2' in protocol_version:
        version = 'HTTP/2'
    else:
        version = 'Unknown'

    return f'The request is using {version}.'


@app.route('/header_contents')
def header_contents():
    # 获取协议版本
    headers = request.headers
    header_contents = '\n'.join([f'{key}: {value}' for key, value in headers.items()])
    print(f"header_contents={header_contents}")
    return header_contents


if __name__ == '__main__':
    # 使用gunicorn设置应用超时时间
    # gunicorn -w 1 -b 127.0.0.1:8000 --timeout 5 http11:app
    app.run(debug=True)