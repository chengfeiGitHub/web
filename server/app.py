from flask import Flask, render_template
from flask_socketio import SocketIO, emit,send
from random import randint

app = Flask(__name__)
socketio = SocketIO(app)

# 主路由
@app.route('/')
def hello():
    data = randint(1, 1000)
    socketio.emit('header_data', {'data': data, 'type':'randint'})
    data = randint(1, 1000)
    socketio.emit('main_data', {'data': data, 'type':'randint'})
    data = randint(1, 1000)
    socketio.emit('menu_data', {'data': data, 'type':'randint'})
    data = randint(1, 1000)
    socketio.emit('footer_data', {'data': data, 'type':'randint'})

    print(data)
    return "刷新页面即将发送 并且发送要给随机数"

# 监听连接
@socketio.on('connect')
def test_connect():
    print('客户端发起连接')

# 监听断开
@socketio.on('disconnect')
def test_disconnect():
    print('连接断开')


# 监听一个事件并绑定一个回调函数
def my_function_handler(data):
    print('消息监听回调函数',str(data))
socketio.on_event('test event', my_function_handler)


if __name__ == '__main__':
    socketio.run(app)
