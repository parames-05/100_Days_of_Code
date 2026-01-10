from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(10), nullable=False) # Format: YYYY-MM-DD

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_tasks/<date>')
def get_tasks(date):
    tasks = Task.query.filter_by(date=date).all()
    return jsonify([{'id': t.id, 'content': t.content} for t in tasks])

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(content=data['content'], date=data['date'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'success': True, 'id': new_task.id})

if __name__ == '__main__':
    app.run(debug=True)