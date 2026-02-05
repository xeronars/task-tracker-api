from flask import Flask, request, jsonify
from models import db, Task
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Task Tracker API running"

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400
    
    task = Task(
        title = data["title"],
        description = data.get("description", "")
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task added"}), 201

@app.route("/tasks", methods=["GET"])
def view_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

if __name__ == "__main__":
    app.run(debug=True)