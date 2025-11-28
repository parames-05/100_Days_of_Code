import turtle, random, math, time

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Chaotic Particle Fountain")
screen.tracer(0, 0)

def make_particle():
    t = turtle.Turtle()
    t.shape("circle")
    t.color(random.random(), random.random(), random.random())
    t.shapesize(0.3)
    t.penup()
    t.speed(0)
    t.goto(0, -300)
    return {
        "t": t,
        "x": 0,
        "y": -300,
        "vx": random.uniform(-3, 3),
        "vy": random.uniform(8, 17),
        "g": random.uniform(0.15, 0.35),
        "drag": random.uniform(0.96, 0.995)
    }

particles = [make_particle() for _ in range(250)]

while True:
    for p in particles:
        p["vx"] += random.uniform(-0.2, 0.2)
        p["vy"] -= p["g"]
        p["vx"] *= p["drag"]
        p["vy"] *= p["drag"]
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        if p["y"] < -320:
            p["x"] = 0
            p["y"] = -300
            p["vx"] = random.uniform(-3, 3)
            p["vy"] = random.uniform(8, 17)
        p["t"].goto(p["x"], p["y"])
    screen.update()
    time.sleep(0.01)
