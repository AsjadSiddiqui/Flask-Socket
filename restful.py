from flask import Flask, jsonify
from flask_socketio import SocketIO, join_room

app = Flask(__name__)

socketio = SocketIO(app)

@app.route("/")
def helloWorld():
  return jsonify({"msg": "Hello World !"})

@app.route("/home/", methods=["GET"])
def hello2():
  return jsonify({"msg": "Hello World !"})

@app.route("/test/", methods=["GET"])
def hello3():
  return "Hello World !"


#===============================================================================================================

@socketio.on("connect")
def connect():
  print("Someone Joined !")
  @socketio.on("connection")
  def joinRoom(data):
    try:
      print(f"A Person, {data['userName']} has joined the Room {data['room']}")
      join_room(data["room"])
    except Exception as e:
      print("ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
      print(e)
      print(data)
    socketio.emit("connected", data)




@socketio.on("msg")
def msgRoom(data):
  socketio.emit("msg", data, room=data["room"])


if __name__ == "__main__":
  socketio.run(app)