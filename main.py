from flask import Flask, request, jsonify
from data_processing.sensor_data import process_sensor_data
from ml_model.predict import predict_performance, assess_injury_risk

app = Flask(__name__)

@app.route('/collect-data', methods=['POST'])
def collect_data():
    sensor_data = request.json
    processed_data = process_sensor_data(sensor_data)
    performance_insights = predict_performance(processed_data)
    injury_risk = assess_injury_risk(processed_data)
    return jsonify({
        'performance_insights': performance_insights,
        'injury_risk': injury_risk
    })

if __name__ == '__main__':
    app.run(debug=True)
