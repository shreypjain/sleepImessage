from flask import Flask, request, jsonify
from sleep import sleepMessage
from py_imessage import imessage
import socket

app = Flask(__name__)
ip = socket.gethostbyname(socket.gethostname())

@app.route('/api/send', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        return(jsonify(sleepMessage(request.form.get("phone"),request.form.get("message"))))
    else:
        return(jsonify(sleepMessage(request.args.get("phone"), request.args.get("message"))))

    # # import pdb; pdb.set_trace();
    # phone = request.form.get("phone")
    # text = request.form.get("text")

    # if text:
    #     message = text
    # else:
    #     message = "Thanks for checking out balto!"
    # # https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    # TODO: write this as a better experienc

    # guid = imessage.send(phone, text)

    # return jsonify({'guid': guid})

@app.route("/api/status/<guid>", methods=['GET'])
def message_status(guid): 
    # search local db for the message here and return date_read, and date_delivered
    message = imessage.status(guid)

    return jsonify(message)

@app.route("/api/is_imessage/<phone>", methods=['GET'])
def is_imessage_capable(phone): 
    return jsonify({'is_imessage': imessage.check_compatibility(phone)})

@app.route('/')
def index():
    return 'Hello Stealth Mode !'

if __name__ == '__main__':
    app.run(host=ip, port=5555)