from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for simplicity
patients = {}

@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.json
    patient_id = data.get("id")
    if not patient_id:
        return jsonify({"error": "Patient ID is required"}), 400
    patients[patient_id] = data
    return jsonify({"message": "Patient created successfully"}), 201

@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = patients.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(patient), 200

@app.route('/patients/<patient_id>', methods=['PUT'])
def update_patient(patient_id):
    if patient_id not in patients:
        return jsonify({"error": "Patient not found"}), 404
    data = request.json
    patients[patient_id].update(data)
    return jsonify({"message": "Patient updated successfully"}), 200

@app.route('/patients', methods=['GET'])
def list_patients():
    return jsonify(list(patients.values())), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
