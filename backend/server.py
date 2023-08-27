from flask import Flask, Response
from flask_cors import CORS
from flask import request
import csv
import json

app = Flask(__name__)
CORS(app, origins='http://localhost:3000', methods=["GET", "POST"])

data_file = './data.csv'

def read_csv_data():
    with open(data_file, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        next(reader)
        data = []
        for row in reader:
            name = row['Name']
            radius = float(row['Radius'])
            mass = float(row['Mass'])
            distance = float(row['Distance'])
            data.append({
                "Name": name,
                "Radius": int(radius),
                "Mass": float(mass),
                "Distance": float(distance),
            })
        return data

@app.route('/get_data', methods=['GET'])
def get_data():
    data = read_csv_data()
    response = Response(json.dumps(data), content_type='application/json')
    return response

@app.route('/update_data', methods=['POST'])
def update_data():
    received_data = request.json
    all_data = read_csv_data()

    for index, row in enumerate(all_data):
        if row["Name"] == received_data["Name"]:
            all_data[index] = received_data
            break
    
    with open(data_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['Name', 'Radius', 'Mass', 'Distance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerheader()
        for row in all_data:
            writer.writerow({
                'Name': row['Name'],
                'Radius': row['Radius'],
                'Mass': row['Mass'],
                'Distance': row['Distance']
            })
            
    response = jsonify({"message": "Data updated successfully"})
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    return response

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)