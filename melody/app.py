from melody.core import MelodyRender
import flask
render_app = flask.Flask(__name__)

@render_app.route('/')
def hello_world():
    render = MelodyRender(render_app.config['markdown_file'])
    html = render.render()
    return html
