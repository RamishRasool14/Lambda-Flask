from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def endpoint():
    try:
        data = request.get_json()

        # Extract values from the incoming request
        arr = data.get('arr')
        target_sum = data.get('sum')

        # Your existing logic to send a request to the external endpoint
        url = "https://vko3cckhgk.execute-api.us-east-1.amazonaws.com/Stage"
        payload = json.dumps({
            "arr": arr,
            "sum": target_sum
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()

        body = response.json()
        if body == []:
            return jsonify({"result": False, "pairs": []}), 200
        return jsonify({"result": True, "pairs": response.json()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
