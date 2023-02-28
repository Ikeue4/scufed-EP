from flask import Flask, request
from datetime import datetime
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/time')
def get_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    response = app.make_response(current_time)
    return response

class TrafficLoggerMiddleware:
    def __init__(self, app):
        self.app = app
        self.traffic_log = []

    def __call__(self, environ, start_response):
        with app.request_context(environ):
            # Log the incoming request
            self.traffic_log.append({
                'method': request.method,
                'url': request.url,
                'body': request.get_data().decode('utf-8')
            })

        # Call the next middleware in the chain
        return self.app(environ, start_response)

# Attach the middleware to the Flask app
app.wsgi_app = TrafficLoggerMiddleware(app.wsgi_app)

# Define a route to view the traffic log
@app.route('/traffic-log')
def traffic_log():
    return {'log': app.wsgi_app.traffic_log}

if __name__ == '__main__':
    app.run()