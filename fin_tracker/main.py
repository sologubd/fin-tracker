from asgiref.wsgi import WsgiToAsgi
from flask import Flask

app = Flask(__name__)


@app.route("/")
async def hello():
    return """
    <!doctype html>
    <html lang="en">
        <head>
            <title>Fintracker</title>
        </head>
        <body>
            <h1>Fin Tracker</h1>
        </body>
    </html>
    """


asgi_app = WsgiToAsgi(app)
