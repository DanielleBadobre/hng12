from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def get_info():
    email = "badobredanielle@gmail.com"
    current_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    github_url = "https://github.com/DanielleBadobre/hng12"

    response = {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)