import turtle, math, time

screen = turtle.Screen()
screen.setup(750, 750)
screen.bgcolor("black")
screen.title("Seven-Planet System")
screen.tracer(0, 0)

def make_body(color, size):
    t = turtle.Turtle()
    t.shape("circle")
    t.color(color)
    t.shapesize(size)
    t.penup()
    t.speed(0)
    return t

sun = make_body("#ffdd44", 2.5)

planets = [
    {"t": make_body("#ff8800", 0.5), "r": 60,  "speed": 0.035, "angle": 0},
    {"t": make_body("#66ccff", 0.55), "r": 95,  "speed": 0.028, "angle": 0},
    {"t": make_body("#22ff55", 0.65), "r": 130, "speed": 0.022, "angle": 0},
    {"t": make_body("#bb88ff", 0.75), "r": 165, "speed": 0.018, "angle": 0},
    {"t": make_body("#ffaa44", 0.9),  "r": 210, "speed": 0.014, "angle": 0},
    {"t": make_body("#44aaff", 1.0),  "r": 255, "speed": 0.011, "angle": 0},
    {"t": make_body("#ff4444", 1.1),  "r": 300, "speed": 0.008, "angle": 0},
]

while True:
    for body in planets:
        body["angle"] += body["speed"]
        x = math.cos(body["angle"]) * body["r"]
        y = math.sin(body["angle"]) * body["r"]
        body["t"].goto(x, y)
    screen.update()
    time.sleep(0.01)
