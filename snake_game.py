import pygame
import random
import math


# Set colors
BLACK = (6, 6, 7)               # snake and text
FUCHSIA = (240, 55, 165)        # food
BACKGROUND = (133, 179, 150)


# Set window dimensions
DIS_WIDTH = 600
DIS_HEIGHT = 400
GAP = 5                         # space between components
BT = 5                          # border thickness
FPS = 24                        # speed of snake   | for easy mode change it with 16
SIZE = 10                       # size of snake and food block


pygame.init()
pygame.display.set_caption('Snake Game')                # window title
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))  # window displayed
clock = pygame.time.Clock()                             # game will not be ended in opening
text = pygame.font.SysFont("poppins", 16, bold=True)


def show_components(score):
    score_text = text.render(" Score: " + str(score), True, BLACK)
    dis.blit(score_text, [GAP, GAP])

    options_text = text.render("R for Replay - Q for Quit.", True, BLACK)
    dis.blit(options_text, [DIS_WIDTH-options_text.get_rect().right-GAP, GAP])

    TH = score_text.get_rect().bottom       # Text height
    TH = TH - TH%SIZE + SIZE
    pygame.draw.rect(dis, BLACK, [GAP, (2*GAP+TH), BT, DIS_HEIGHT-(2*GAP+TH)-GAP])                  # left-wall
    pygame.draw.rect(dis, BLACK, [DIS_WIDTH-(GAP+BT), (2*GAP+TH), BT, DIS_HEIGHT-(2*GAP+TH)-GAP])   # right-wall
    pygame.draw.rect(dis, BLACK, [GAP, (GAP+TH), DIS_WIDTH-2*GAP, BT])                              # top-wall
    pygame.draw.rect(dis, BLACK, [GAP, DIS_HEIGHT-GAP-BT, DIS_WIDTH-2*GAP, BT])                     # bottom-wall


def get_border_values(text):
    temp = text.render("Not seen on screen, just for calculation.", True, BLACK)
    TH = temp.get_rect().bottom
    TH = TH - TH%SIZE + SIZE

    XLOWEST = GAP + BT
    XHIGHEST = DIS_WIDTH - GAP - BT
    YLOWEST = GAP + TH + BT
    YHIGHEST = DIS_HEIGHT - GAP - BT

    return XLOWEST, XHIGHEST, YLOWEST, YHIGHEST


def show_controls():
    mesg = text.render('Use the arrow keys to control the snake', True, BLACK)
    pos = mesg.get_rect(center=(DIS_WIDTH/2, DIS_HEIGHT/4))
    dis.blit(mesg, pos)


def show_game_over_message():
    mesg = text.render("Game Over", True, BLACK)
    pos = mesg.get_rect(center=(DIS_WIDTH/2, DIS_HEIGHT/2))
    dis.blit(mesg, pos)


def next_food(borders, snake):
    XLOWEST, XHIGHEST, YLOWEST, YHIGHEST = borders
    while True:
        foodx = math.floor(random.randrange(XLOWEST, XHIGHEST) / 10.0) * 10.0
        foody = math.floor(random.randrange(YLOWEST, YHIGHEST) / 10.0) * 10.0

        if [foodx, foody] not in snake:
            return foodx, foody


def show_food(foodx, foody):
    pygame.draw.rect(dis, FUCHSIA, [foodx, foody, SIZE, SIZE])


def show_snake(snake):
    for x in snake:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], SIZE, SIZE])
        # pygame.draw.rect(dis, BLACK, [x[0]+0.1, x[1]+0.1, SIZE-0.1, SIZE-0.1])


def listen_events(running, waiting, game_over, dx, dy):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            game_over = False
            waiting = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
                game_over = False
            elif event.key == pygame.K_r:
                gameLoop()
            elif event.key == pygame.K_LEFT:
                dx = -SIZE
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = SIZE
                dy = 0
            elif event.key == pygame.K_UP:
                dy = -SIZE
                dx = 0
            elif event.key == pygame.K_DOWN:
                dy = SIZE
                dx = 0
            waiting = False
    return running, waiting, game_over, dx, dy


def check_game_over(x, y, snake):
    if x >= XHIGHEST or x < XLOWEST or y >= YHIGHEST or y < YLOWEST or [x, y] in snake[:-1]:
       return True
    return False


def update_screen(waiting, game_over, score, snake, foodx, foody):
    dis.fill(BACKGROUND)
    show_components(score)

    if waiting:
        show_controls()

    if game_over:
        show_game_over_message()
    else:
        show_snake(snake)
        show_food(foodx, foody)

    pygame.display.update()



def gameLoop():
    global XLOWEST, XHIGHEST, YLOWEST, YHIGHEST
    XLOWEST, XHIGHEST, YLOWEST, YHIGHEST = borders = get_border_values(text)

    running = True              # MOST GENERAL - PROGRAM IS ACTIVE
    waiting = True              # IN THE BEGINING WAIT FOR FIRST ACTION
    game_over = False           # SNAKE IS ALIVE

    x = DIS_WIDTH/2 - 9*SIZE
    y = DIS_HEIGHT/2
    dx = 0                      # delta x
    dy = 0                      # delta y

    _snake = []
    length = 1
    for _ in range(5):
        x += SIZE
        _snake.append([x, y])
        length += 1

    score = 0
    foodx, foody = next_food(borders, _snake)

    
    while waiting:
        update_screen(waiting, game_over, score, _snake, foodx, foody)
        running, waiting, game_over, dx, dy = \
            listen_events(running, waiting, game_over, dx, dy)

    while running:
        game_over = check_game_over(x, y, _snake)

        while game_over:
            update_screen(waiting, game_over, score, _snake, foodx, foody)
            running, waiting, game_over, dx, dy = listen_events(running, waiting, game_over, dx, dy)
        

        running, waiting, game_over, dx, dy = \
            listen_events(running, waiting, game_over, dx, dy)

        x += dx
        y += dy
        _snake.append([x, y])
        
        if len(_snake) > length:
            del _snake[0]

        if x == foodx and y == foody:
            foodx, foody = next_food(borders, _snake)
            length += 1
            score += 1


        update_screen(waiting, game_over, score, _snake, foodx, foody)
        clock.tick(FPS)

    pygame.quit()
    quit()

if __name__ == '__main__':
    gameLoop()
