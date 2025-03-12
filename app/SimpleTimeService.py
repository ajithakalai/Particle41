from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_json():
    response = {
        "App Name": "SimpleTimeServices",
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.remote_addr,
        #"real_ip": request.headers.get("X-Forwarded-For")
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)