from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='myredis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    redis.expire('hits', 6600) 
    return '你好! 我們見過 %s 次面。' % str(redis.get('hits'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5800)
