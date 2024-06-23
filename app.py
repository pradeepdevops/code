from Flask import Flask
from redis import Redis

app = Flask(__name__)
#Try host='redis' if things dont work
redis = Redis(host='172.17.0.1', port=6379)

@app.route('/')
def hello():
  count = redis.incr('hits')
  return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
