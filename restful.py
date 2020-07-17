from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def helloWorld():
  return jsonify({"msg": "Hello World !"})

@app.route("/home/", methods=["GET"])
def hello2():
  return jsonify({"msg": "Hello World !"})

@app.route("/test/", methods=["GET"])
def hello3():
  return "Hello World !"


if __name__ == "__main__":
  app.run()