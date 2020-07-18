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
  #LEFT IT HERE!
  query = request.args.get('query')
  name = request.args.getlist('name')
  name2 = request.args[0]['name']
  name3 = request.args['name']
  room = request.args.getlist('room[]')
  print(name)
  print(name2)
  print(name3)
  print(room)
  print(request.args)
  # emit("connect", "HI")
  emit("connected", "Hello There!")


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


if __name__ == "__main__":
  socketio.run(app)