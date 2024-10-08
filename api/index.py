from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

def load_data():
    data_csv = pd.read_csv('data/data.csv')
    return data_csv.to_dict('records')

dummy_data = load_data()

@app.route('/api/data', methods=['GET'])
def get_person_data():
    nik = request.args.get('nik')

    if not nik:
        return jsonify({"message": "NIK parameter is required"}), 400

    person_data = next((item for item in dummy_data if str(item['nik']) == nik), None)

    if not person_data:
        return jsonify({"message": "Person not found"}), 404

    return jsonify(person_data)

if __name__ == '__main__':
    app.run(debug=False)