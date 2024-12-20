from flask import Flask, request, jsonify

app = Flask(__name__)

notifications = []

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.json
    notifications.append(data)
    return jsonify({"message": "Notification sent successfully"}), 201

@app.route('/notifications', methods=['GET'])
def list_notifications():
    return jsonify(notifications), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
