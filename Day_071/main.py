from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# -----------------------
# Database Model
# -----------------------
class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

# -----------------------
# Create Tables
# -----------------------
with app.app_context():
    db.create_all()

# -----------------------
# CREATE
# -----------------------
@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()

    if not data or "title" not in data or "content" not in data:
        abort(400, "Title and content are required")

    note = Note(
        title=data["title"],
        content=data["content"]
    )

    db.session.add(note)
    db.session.commit()

    return jsonify(note.to_dict()), 201

# -----------------------
# READ (ALL)
# -----------------------
@app.route("/notes", methods=["GET"])
def get_notes():
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return jsonify([note.to_dict() for note in notes])

# -----------------------
# READ (ONE)
# -----------------------
@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = Note.query.get_or_404(note_id)
    return jsonify(note.to_dict())

# -----------------------
# UPDATE
# -----------------------
@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    data = request.get_json()

    if not data:
        abort(400, "No data provided")

    if "title" in data:
        note.title = data["title"]

    if "content" in data:
        note.content = data["content"]

    db.session.commit()
    return jsonify(note.to_dict())

# -----------------------
# DELETE
# -----------------------
@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)

    db.session.delete(note)
    db.session.commit()

    return jsonify({"message": "Note deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
