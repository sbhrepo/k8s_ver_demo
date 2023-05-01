import configuration
import socket
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    response = {"status": "success", "version": configuration.version, "hostname": hostname, "IP address": ipaddress}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)