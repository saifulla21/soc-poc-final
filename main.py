import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = False
socketio = SocketIO(app,engineio_logger=False,log_output=False,async_mode='eventlet')

@app.route('/')
def hello_world():
  return 'Hello, World!'

@socketio.on('myevent')
def test_message(message):
    emit('myresponse', {'data': 'got it!'})
    
@socketio.on('chat message')
def test_message(message):
    emit('chat message', message)

if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0",port=int(os.environ["PORT"].rstrip()))
