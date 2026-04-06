from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

DB_FILE = "database.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f: return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, "w") as f: json.dump(db, f)

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    uid = str(data.get("id"))
    db = load_db()
    db[uid] = data
    save_db(db)
    return jsonify({"status": "ok"})

@app.route('/get_data', methods=['GET'])
def get_data():
    uid = str(request.args.get("id"))
    db = load_db()
    return jsonify(db.get(uid, {"id": uid, "dogs": 0, "gh": 100, "refs": 0}))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
