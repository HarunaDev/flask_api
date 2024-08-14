from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Home"

# create route with http parameter
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Smith",
        "email": "john.smith@ecu.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        return jsonify(user_data), 200