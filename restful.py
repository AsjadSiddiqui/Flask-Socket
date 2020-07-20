from flask import Flask, jsonify, request, Response
from flask_socketio import SocketIO, join_room, emit, send

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
  query = request.args
  data = query.to_dict()

  userName = data["name"]
  room = data["room"]
  userInfo = {
    "name": userName,
    "room": room
  }
  # emit("connect", "HI")
  emit("connected", userInfo)


@socketio.on("hola")
def joinRoom(data):
  print("HOLA CALLED SERVER ======================================================================")
  print(data)
  try:
    print(f"A Person, {data['userName']} has joined the Room {data['room']}")
    join_room(data["room"])
  except Exception as e:
    print("ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    print(e)
    print(data)
  emit("connected", data)


@socketio.on("msg")
def msgRoom(data):
  emit("msg", data, room=data["room"])

@socketio.on("newMsg")
def msgRoom(data):
  print(data)
  emit("newMsg", data)


if __name__ == "__main__":
  socketio.run(app)