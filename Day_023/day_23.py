import turtle, math, random, sys

axiom = "X"
rules = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF"
}
iterations = 6
angle = 25
step = 5
jitter = 0.8
width_start = 8
width_end = 1
palette = [(68, 36, 18), (96, 55, 24), (140, 90, 40), (34, 139, 34), (50, 205, 50), (173, 255, 47)]

def generate(axiom, rules, n):
    s = axiom
    for _ in range(n):
        s = "".join(rules[c] if c in rules else c for c in s)
    return s

def interp_color(t):
    n = len(palette)-1
    if t >= 1: return palette[-1]
    i = int(t * n)
    a = t * n - i
    r1,g1,b1 = palette[i]
    r2,g2,b2 = palette[i+1]
    return (int(r1 + (r2-r1)*a), int(g1 + (g2-g1)*a), int(b1 + (b2-b1)*a))

def rgbhex(c):
    return "#%02x%02x%02x" % c

def draw_lsystem(s, turt, length, ang, jitter_amt):
    stack = []
    total = len([ch for ch in s if ch == "F"])
    drawn = 0
    for ch in s:
        if ch == "F":
            jitter_len = length * (1 + random.uniform(-jitter_amt, jitter_amt))
            turt.forward(jitter_len)
            drawn += 1
            frac = drawn/total if total else 0
            color = interp_color(frac)
            turt.pencolor(rgbhex(color))
            penw = width_start * (1-frac) + width_end * frac
            turt.pensize(max(1, penw))
        elif ch == "X":
            pass
        elif ch == "+":
            turt.right(ang + random.uniform(-1,1))
        elif ch == "-":
            turt.left(ang + random.uniform(-1,1))
        elif ch == "[":
            pos = turt.position()
            head = turt.heading()
            ps = turt.pensize()
            col = turt.pencolor()
            stack.append((pos, head, ps, col))
        elif ch == "]":
            pos, head, ps, col = stack.pop()
            turt.penup()
            turt.setposition(pos)
            turt.setheading(head)
            turt.pendown()
            turt.pensize(ps)
            turt.pencolor(col)

def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=1000, height=800)
    screen.title("L-System Fractal Garden")
    screen.bgcolor("#0a0a0a")
    screen.tracer(0,0)
    return screen

def make_turtle():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.setpos(0, -350)
    t.pendown()
    return t

def main():
    random.seed(42)
    s = generate(axiom, rules, iterations)
    screen = setup_screen()
    t = make_turtle()
    length = 8
    draw_lsystem(s, t, length, angle, jitter)
    screen.update()
    turtle.done()

if __name__ == "__main__":
    main()
