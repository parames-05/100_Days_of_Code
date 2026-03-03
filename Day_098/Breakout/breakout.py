import pygame
import random
import math
import sys

pygame.init()
pygame.font.init()

WIDTH = 1100
HEIGHT = 700
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Elite Edition")

clock = pygame.time.Clock()
BG_COLOR = (18, 18, 30)
WHITE = (255, 255, 255)
NEON_BLUE = (0, 200, 255)
NEON_PINK = (255, 0, 180)
NEON_GREEN = (0, 255, 140)
BRICK_COLORS = [(255, 87, 51), (255, 195, 0), (0, 200, 255), (140, 255, 0)]
TITLE_FONT = pygame.font.SysFont("arialblack", 80)
BUTTON_FONT = pygame.font.SysFont("arial", 50)
GAME_FONT = pygame.font.SysFont("arial", 28)


class Paddle:
    def __init__(self):
        self.width = 150
        self.height = 20
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 80
        self.speed = 10

    def draw(self):
        pygame.draw.rect(screen, NEON_BLUE, (self.x, self.y, self.width, self.height), border_radius=10)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed


class Ball:
    def __init__(self):
        self.radius = 10
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = 6 * random.choice((-1, 1))
        self.speed_y = -6

    def draw(self):
        pygame.draw.circle(screen, NEON_PINK, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x >= WIDTH:
            self.speed_x *= -1
        if self.y <= 0:
            self.speed_y *= -1


class Brick:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 90, 30)
        self.color = color
        self.alive = True

    def draw(self):
        if self.alive:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=6)


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(3, 6)
        self.speed_x = random.uniform(-4, 4)
        self.speed_y = random.uniform(-4, 4)
        self.life = 30

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.life -= 1

    def draw(self):
        if self.life > 0:
            pygame.draw.circle(screen, NEON_GREEN, (int(self.x), int(self.y)), self.size)



def create_bricks():
    bricks = []
    for row in range(6):
        for col in range(10):
            x = 100 + col * 95
            y = 80 + row * 40
            color = BRICK_COLORS[row % len(BRICK_COLORS)]
            bricks.append(Brick(x, y, color))
    return bricks

def landing_page():
    while True:
        screen.fill(BG_COLOR)

        title = TITLE_FONT.render("BREAKOUT", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//3))

        button_rect = pygame.Rect(WIDTH//2 - 150, HEIGHT//2, 300, 80)
        pygame.draw.rect(screen, NEON_BLUE, button_rect, border_radius=12)

        button_text = BUTTON_FONT.render("START", True, WHITE)
        screen.blit(button_text, (button_rect.centerx - button_text.get_width()//2,
                                  button_rect.centery - button_text.get_height()//2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return


def game():
    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks()
    particles = []
    score = 0
    lives = 3

    running = True

    while running:
        clock.tick(FPS)
        screen.fill(BG_COLOR)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        paddle.move(keys)
        ball.move()

        if pygame.Rect(paddle.x, paddle.y, paddle.width, paddle.height).collidepoint(ball.x, ball.y):
            ball.speed_y *= -1

        for brick in bricks:
            if brick.alive and brick.rect.collidepoint(ball.x, ball.y):
                brick.alive = False
                ball.speed_y *= -1
                score += 10

                for _ in range(15):
                    particles.append(Particle(ball.x, ball.y))

        for particle in particles:
            particle.update()
            particle.draw()

        if ball.y > HEIGHT:
            lives -= 1
            ball = Ball()
            if lives == 0:
                return score

        paddle.draw()
        ball.draw()
        for brick in bricks:
            brick.draw()

        score_text = GAME_FONT.render(f"Score: {score}", True, WHITE)
        lives_text = GAME_FONT.render(f"Lives: {lives}", True, WHITE)
        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (WIDTH - 120, 20))

        pygame.display.update()


def game_over_screen(score):
    while True:
        screen.fill(BG_COLOR)

        over_text = TITLE_FONT.render("GAME OVER", True, WHITE)
        screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//3))

        score_text = BUTTON_FONT.render(f"Score: {score}", True, NEON_GREEN)
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - 40))

        restart_text = GAME_FONT.render("Click Anywhere to Restart", True, WHITE)
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

def main():
    while True:
        landing_page()
        score = game()
        game_over_screen(score)

main()