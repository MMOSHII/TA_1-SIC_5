from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/sound', methods=['POST'])
def sound_data():
    data = request.json
    if 'sound_level' in data:
        sound_level = data['sound_level']
        print(f"Received sound level: {sound_level}")
        return jsonify({"status": "success", "sound_level": sound_level}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')
