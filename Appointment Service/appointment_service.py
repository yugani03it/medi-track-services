from flask import Flask, request, jsonify

app = Flask(__name__)

appointments = {}

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    appointment_id = data.get("id")
    if not appointment_id:
        return jsonify({"error": "Appointment ID is required"}), 400
    appointments[appointment_id] = data
    return jsonify({"message": "Appointment created successfully"}), 201

@app.route('/appointments/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = appointments.get(appointment_id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    return jsonify(appointment), 200

@app.route('/appointments', methods=['GET'])
def list_appointments():
    return jsonify(list(appointments.values())), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
