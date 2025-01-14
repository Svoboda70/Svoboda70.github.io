from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

VERIFICATION_TOKEN = "your_verification_token"
ENDPOINT = "https://svoboda70.github.io/validate.html"

@app.route("/", methods=["GET"])
def handle_challenge():
    challenge_code = request.args.get("challenge_code")
    if not challenge_code:
        return jsonify({"error": "challenge_code is missing"}), 400
    
    hash_object = hashlib.sha256()
    hash_object.update(challenge_code.encode('utf-8'))
    hash_object.update(VERIFICATION_TOKEN.encode('utf-8'))
    hash_object.update(ENDPOINT.encode('utf-8'))
    challenge_response = hash_object.hexdigest()

    return jsonify({"challengeResponse": challenge_response}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)