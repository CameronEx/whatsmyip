from flask import Flask, request, Response

# Initialize the Flask application
app = Flask(__name__)

# Default route, print user's IP
@app.route('/')

def index():
  ip = request.remote_addr
  data = { "user_ip":ip }
  resp = Response(response=data['user_ip'], status=200, mimetype="application/json")
  return(resp)


if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("8081")
  )




