import turtle, random, time

cell = 20
rows = 21
cols = 21

screen = turtle.Screen()
screen.setup(cols*cell + 50, rows*cell + 50)
screen.bgcolor("black")
screen.title("Recursive Maze Generator and Solver")
screen.tracer(0, 0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)
pen.color("white")

walker = turtle.Turtle()
walker.shape("circle")
walker.color("cyan")
walker.shapesize(0.45)
walker.penup()
walker.speed(0)

maze = [[1 for _ in range(cols)] for _ in range(rows)]

def draw_cell(r, c):
    x = -cols*cell//2 + c*cell
    y = rows*cell//2 - r*cell
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x+cell, y)
    pen.goto(x+cell, y-cell)
    pen.goto(x, y-cell)
    pen.goto(x, y)

def carve(r, c):
    maze[r][c] = 0
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    random.shuffle(dirs)
    for dr, dc in dirs:
        nr, nc = r + dr*2, c + dc*2
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1:
            maze[r+dr][c+dc] = 0
            carve(nr, nc)

def draw_maze():
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                draw_cell(r, c)
    screen.update()

path = []

def solve(r, c):
    if r == rows-2 and c == cols-2:
        path.append((r,c))
        return True
    if maze[r][c] != 0 or (r,c) in path:
        return False
    path.append((r,c))
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        if solve(r+dr, c+dc):
            return True
    path.pop()
    return False

def show_solution():
    for r, c in path:
        x = -cols*cell//2 + c*cell + cell/2
        y = rows*cell//2 - r*cell - cell/2
        walker.goto(x, y)
        screen.update()
        time.sleep(0.02)

random.seed()
carve(1,1)
draw_maze()
solve(1,1)
show_solution()

turtle.done()
