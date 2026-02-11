from flask import Flask
from redis import Redis

app = Flask(__name__)
# Connect to Redis container named 'redis'
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # Increase counter every refresh
    count = redis.incr('hits')
    return f"<h1>Hello! You have seen this page {count} times.</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)