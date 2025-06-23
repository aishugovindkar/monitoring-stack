from flask import Flask
import logging
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Setup Prometheus metrics
metrics = PrometheusMetrics(app)

# Setup structured logging
logging.basicConfig(
    filename='app.log',  # Filebeat will pick this
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO
)

@app.route('/')
def home():
    app.logger.info("Home page was accessed")
    return "Hello from Flask App!"

@app.route('/error')
def error():
    app.logger.error("This is an error example")
    return "This is an error!", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

