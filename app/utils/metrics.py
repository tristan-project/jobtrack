from prometheus_client import Summary, start_http_server, Counter

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
login_request_counter = Counter('auth_login_requests_total', 'Total number of /auth/login requests')



# Start up the server to expose the metrics.
def start_metrics_server(port=8001):
    start_http_server(port)