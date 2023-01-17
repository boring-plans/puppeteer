"""
Flask app.

By Allen Tao
Created at 2023/01/17 14:05
"""
from apiflask import APIFlask
from flask import Response, render_template, request
from flask_cors import CORS

from km import mouse_down, mouse_up, mouse_to
from stream import gen_stream

app = APIFlask(__name__)
CORS(app)


@app.get('/frame')
def get_frame():
    return Response(gen_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.put('/mousedown-event')
def create_mousedown_event():
    [x, y] = request.get_json().get('pos')
    mouse_down(x, y)
    return 'DONE', 201


@app.put('/mouseup-event')
def create_mouseup_event():
    mouse_up()
    return 'DONE', 201


@app.put('/mouseto-event')
def create_mouseto_event():
    [x, y] = request.get_json().get('pos')
    mouse_to(x, y)
    return 'DONE', 201


@app.get('/')
def index():
    return 'Hi there~'
