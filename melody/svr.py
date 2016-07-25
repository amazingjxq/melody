from gevent.wsgi import WSGIServer
from melody.app import render_app

def run_server(markdown_file):
    render_app.config["markdown_file"] = markdown_file
    http_server = WSGIServer(('', 5000), render_app)
    http_server.serve_forever()
