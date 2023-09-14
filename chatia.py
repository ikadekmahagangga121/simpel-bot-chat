from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/api/v1/dialogue', methods=['POST'])
def dialogue():
 body = request.json['body']
 params = {'prompt': 'What do you want to know?'}
 response = requests.post(f"https://api.openai.com/reinforcement-learning-platform/api/v1/dialogue", data={'params': params})
 if response.status_code == 200:
    return response.json()
 else:
    return f"Error: {response.status_code}n{response.reason}"
if __name__ == '__main__':
 app.run(debug=True)
