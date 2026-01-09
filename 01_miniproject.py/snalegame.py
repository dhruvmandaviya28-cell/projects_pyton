import pygame
import random
import sys

# ---------- INITIAL SETUP ----------
pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# ---------- COLORS ----------
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

# ---------- FUNCTIONS ----------
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, CELL, CELL))

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    text = font.render("Game Over! Press Q or C", True, RED)
    screen.blit(text, (WIDTH // 6, HEIGHT // 3))
    pygame.display.update()

# ---------- MAIN GAME ----------
def main():
    snake = [[100, 100]]
    direction = "RIGHT"

    food = [
        random.randrange(0, WIDTH, CELL),
        random.randrange(0, HEIGHT, CELL)
    ]

    score = 0
    running = True

    while running:
        screen.fill(BLACK)

        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # MOVE SNAKE
        head_x, head_y = snake[0]

        if direction == "UP":
            head_y -= CELL
        elif direction == "DOWN":
            head_y += CELL
        elif direction == "LEFT":
            head_x -= CELL
        elif direction == "RIGHT":
            head_x += CELL

        new_head = [head_x, head_y]

        # COLLISION WITH WALL
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            game_over()
            wait_for_input()
            return

        # COLLISION WITH SELF
        if new_head in snake:
            game_over()
            wait_for_input()
            return

        snake.insert(0, new_head)

        # FOOD
        if new_head == food:
            score += 1
            food = [
                random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL)
            ]
        else:
            snake.pop()

        # DRAW
        draw_snake(snake)
        pygame.draw.rect(screen, RED, (*food, CELL, CELL))
        show_score(score)

        pygame.display.update()
        clock.tick(10)

def wait_for_input():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_c:
                    main()

# ---------- START ----------
main()
pygame.quit()
sys.exit()  