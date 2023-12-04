from SauES import SauES
from flask import Flask, request, jsonify
from time import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        key = request.json['key']
        plain_text = request.json['text']

        sauES = SauES(key)

        start_time = time()
        cypher_text = sauES.encrypt(plain_text)
        end_time = time()

        return jsonify({
            'cypher_text': cypher_text, 
            'time_taken': f'{round((end_time - start_time) * 1000, 2)}ms'
            })
    
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Invalid request'}), 400

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        key = request.json['key']
        cypher_text = request.json['text']

        sauES = SauES(key)

        start_time = time()
        plain_text = sauES.decrypt(cypher_text)
        end_time = time()

        return jsonify({
            'plain_text': plain_text, 
            'time_taken': f'{round((end_time - start_time) * 1000, 2)}ms'
            })
    
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)