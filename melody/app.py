from melody.core import MelodyRender
import flask
from flask import request
render_app = flask.Flask(__name__)

@render_app.route('/')
def hello_world():
    template = request.args.get('template')
    render = MelodyRender(render_app.config['markdown_file'])

    if template:
        html = render.render(template)
    else:
        html = render.render()

    return html

@render_app.route('/static/<path>')
def serve_image(path):
    return flask.send_from_directory(render_app.config['static_dir'], path)
