from flask import Flask, request, jsonify
from models import db, Task

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Task Tracker API running"

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    task = Task(
        title = data["title"],
        description = data["description"]
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task added"}), 201

if __name__ == "__main__":
    app.run(debug=True)