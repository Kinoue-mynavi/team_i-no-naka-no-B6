from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
   return jsonify({ "language": "python" })

if __name__ == "__main__":
    app.run()


print("")