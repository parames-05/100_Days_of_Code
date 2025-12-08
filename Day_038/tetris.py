import tkinter as tk
import random

CELL = 30
COLS = 10
ROWS = 20
SPEED = 500

SHAPES = {
    'I': [[(0,1),(1,1),(2,1),(3,1)],
          [(2,0),(2,1),(2,2),(2,3)]],
    'O': [[(1,0),(2,0),(1,1),(2,1)]],
    'T': [[(1,0),(0,1),(1,1),(2,1)],
          [(1,0),(1,1),(2,1),(1,2)],
          [(0,1),(1,1),(2,1),(1,2)],
          [(1,0),(0,1),(1,1),(1,2)]],
    'L': [[(0,0),(0,1),(1,1),(2,1)],
          [(1,0),(2,0),(1,1),(1,2)],
          [(0,1),(1,1),(2,1),(2,2)],
          [(1,0),(1,1),(1,2),(0,2)]],
    'J': [[(2,0),(0,1),(1,1),(2,1)],
          [(1,0),(1,1),(1,2),(2,2)],
          [(0,1),(1,1),(2,1),(0,2)],
          [(0,0),(1,0),(1,1),(1,2)]],
    'S': [[(1,0),(2,0),(0,1),(1,1)],
          [(1,0),(1,1),(2,1),(2,2)]],
    'Z': [[(0,0),(1,0),(1,1),(2,1)],
          [(2,0),(1,1),(2,1),(1,2)]],
}

class Piece:
    def __init__(self):
        self.shape = random.choice(list(SHAPES.keys()))
        self.rot = 0
        self.x = 3
        self.y = 0

    @property
    def blocks(self):
        return SHAPES[self.shape][self.rot]

    def rotate(self):
        self.rot = (self.rot + 1) % len(SHAPES[self.shape])

class Tetris:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=COLS*CELL, height=ROWS*CELL, bg="black")
        self.canvas.pack()
        root.bind("<Left>", self.move_left)
        root.bind("<Right>", self.move_right)
        root.bind("<Down>", self.move_down)
        root.bind("<Up>", self.rotate)

        self.board = [[None]*COLS for _ in range(ROWS)]
        self.running = True
        self.new_piece()
        self.game_loop()

    def new_piece(self):
        self.piece = Piece()
        if not self.valid_pos(self.piece):
            self.running = False

    def valid_pos(self, piece):
        for x,y in piece.blocks:
            px = piece.x + x
            py = piece.y + y
            if px < 0 or px >= COLS or py < 0 or py >= ROWS:
                return False
            if self.board[py][px] is not None:
                return False
        return True

    def lock_piece(self):
        for x,y in self.piece.blocks:
            self.board[self.piece.y+y][self.piece.x+x] = "gray"
        self.clear_lines()
        self.new_piece()

    def clear_lines(self):
        new = [row for row in self.board if any(c is None for c in row)]
        lines_cleared = ROWS - len(new)
        for _ in range(lines_cleared):
            new.insert(0, [None]*COLS)
        self.board = new

    def move_left(self, e=None):
        self.piece.x -= 1
        if not self.valid_pos(self.piece):
            self.piece.x += 1
        self.draw()

    def move_right(self, e=None):
        self.piece.x += 1
        if not self.valid_pos(self.piece):
            self.piece.x -= 1
        self.draw()

    def move_down(self, e=None):
        self.piece.y += 1
        if not self.valid_pos(self.piece):
            self.piece.y -= 1
            self.lock_piece()
        self.draw()

    def rotate(self, e=None):
        old = self.piece.rot
        self.piece.rotate()
        if not self.valid_pos(self.piece):
            self.piece.rot = old
        self.draw()

    def game_loop(self):
        if not self.running:
            self.game_over()
            return
        self.move_down()
        self.root.after(SPEED, self.game_loop)

    def draw(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                if self.board[r][c]:
                    self.draw_cell(c, r, self.board[r][c])
        for x,y in self.piece.blocks:
            self.draw_cell(self.piece.x+x, self.piece.y+y, "cyan")

    def draw_cell(self, x, y, color):
        x1 = x*CELL; y1 = y*CELL
        self.canvas.create_rectangle(x1,y1,x1+CELL,y1+CELL, fill=color, outline="black")

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(COLS*CELL//2, ROWS*CELL//2,
            text="GAME OVER", fill="white", font=("Arial", 24))

root = tk.Tk()
root.title("Tetris")
Tetris(root)
root.mainloop()
