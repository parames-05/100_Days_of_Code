from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

SAMPLE_TEXT = '''The lighthouse had not blinked in decades, yet tonight it hummed like a throat clearing before speech.
The sea was perfectly still, as if listening.
Inside the tower, the spiral staircase descended farther than architecture should allow.
Every step down made the air colder, and slightly older.
There were footprints in the dust, but they spiraled upward, not down.
At the bottom, a door stood ajar, breathing faintly.
Beyond it was not water, not rock, not sky
but a vast pupil widening at the sound of my name.'''

# Leaderboard file
LEADERBOARD_FILE = "leaderboard.txt"

# Ensure leaderboard file exists
if not os.path.exists(LEADERBOARD_FILE):
    open(LEADERBOARD_FILE, 'w').close()


@app.route('/')
def index():
    return render_template('index.html', sample_text=SAMPLE_TEXT)


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    user_input = data.get('input_string', '')
    time_remaining = data.get('time_left', 0)
    username = data.get('username', 'Anonymous')

    seconds_elapsed = 60 - time_remaining
    if seconds_elapsed <= 0:
        seconds_elapsed = 1  # Prevent division by zero

    # --------- WPM Calculation ----------
    words = len(user_input.strip().split()) if user_input.strip() else 0
    wpm = round(words / (seconds_elapsed / 60))

    # --------- Accuracy Calculation ----------
    errors = 0
    for i in range(len(user_input)):
        if i < len(SAMPLE_TEXT):
            if user_input[i] != SAMPLE_TEXT[i]:
                errors += 1
        else:
            errors += 1  # Over-typing counts as errors

    if len(user_input) > 0:
        accuracy = max(0, round(((len(user_input) - errors) / len(user_input)) * 100))
    else:
        accuracy = 0

    # --------- Save to TXT Leaderboard ----------
    with open(LEADERBOARD_FILE, 'a') as f:
        f.write(f"{username},{wpm},{accuracy}\n")

    return jsonify({
        'wpm': wpm,
        'accuracy': accuracy
    })


@app.route('/leaderboard')
def leaderboard():
    players = []

    with open(LEADERBOARD_FILE, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 3:
                name, wpm, accuracy = parts
                players.append({
                    "name": name,
                    "wpm": int(wpm),
                    "accuracy": int(accuracy)
                })

    # Sort by WPM first, then by Accuracy
    players = sorted(players, key=lambda x: (-x['wpm'], -x['accuracy']))

    top_three = players[:3]

    return render_template('leaderboard.html', players=top_three)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port = 5001)