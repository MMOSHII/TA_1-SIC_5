from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    data = request.get_json()
    if not data or 'temperature' not in data:
        return jsonify({'error': 'Bad request'}), 400
    
    temperature = data['temperature']
    print(f"Received temperature: {temperature}")

    return jsonify({'message': 'Temperature data received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
