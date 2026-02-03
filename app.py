from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://tasks.db"

db = SQLAlchemy(app)

@app.route("/")
def home():
    return "Task Tracker API running"

if __name__ == "__main__":
    app.run(debug=True)