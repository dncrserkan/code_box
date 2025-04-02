import pygame


BACKGROUND = (186, 173, 160)
FONT_COLOR = (118, 109, 90)
BLACK = (6, 6, 7)
TRANSPARENT = (255, 255, 255, 128)


DIS_WIDTH = 420
DIS_HEIGHT = 480
GAP = 10

IMG = pygame.image.load('files/png/base.png')
_box = pygame.image.load('files/png/box.png')


BOXES = {
    '0' : (0, pygame.image.load('files/png/box.png')),
    '2' : (2, pygame.image.load('files/png/box2.png')),
    '4' : (4, pygame.image.load('files/png/box4.png')),
    '8' : (8, pygame.image.load('files/png/box8.png')),
    '16' : (16, pygame.image.load('files/png/box16.png')),
    '32' : (32, pygame.image.load('files/png/box32.png')),
    '64' : (64,pygame.image.load('files/png/box64.png')),
    '128' : (128, pygame.image.load('files/png/box128.png')),
    '256' : (256, pygame.image.load('files/png/box256.png')),
    '512' : (512, pygame.image.load('files/png/box512.png')),
    '1024' : (1024, pygame.image.load('files/png/box1024.png')),
    '2048' : (2048, pygame.image.load('files/png/box2048.png'))}


IMG_H = IMG.get_height()
BOX_H = _box.get_height()
BOX_W = _box.get_width()

IMG_POS = (GAP, DIS_HEIGHT-GAP-IMG_H)
FIRST_BOX_POS = (2*GAP, DIS_HEIGHT-GAP-IMG_H+GAP)




pygame.init()
pygame.display.set_caption('2048 Game')                             # window title
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))              # window displayed
surf = pygame.Surface((DIS_WIDTH, DIS_HEIGHT), pygame.SRCALPHA)     # game over and winn message background surface
surf.fill(TRANSPARENT)


text = pygame.font.SysFont("poppins", 32, bold=True)                # score
text_go = pygame.font.SysFont("poppins", 40, bold=True)             # game over message
text_opt = pygame.font.SysFont("poppins", 16, bold=True)            # options and notes


_newgame = text_opt.render('N - New Game', True, FONT_COLOR)                              # Temp - will be dynamic color in show_score
pos_newgame = (DIS_WIDTH - (2 * GAP + _newgame.get_width()), GAP)
pos_exit = (DIS_WIDTH - (2 * GAP + _newgame.get_width()), GAP + _newgame.get_height())
_note = text_opt.render('Currently, the maximum value is reached.', True, BLACK)          # Temp - used for calculation of note position   
pos_note_first= (GAP, DIS_HEIGHT-2*_note.get_height()-GAP)
pos_note_second = (GAP, DIS_HEIGHT-_note.get_height()-GAP)



dis.fill(BACKGROUND)
dis.blit(IMG, IMG_POS)


def fill_box(num, pos_x, pos_y):
    for val, box in BOXES.values():
        if num == val:
            dis.blit(box, (pos_x, pos_y))
            return


def show_boxes(grid):
    dis.fill(BACKGROUND)
    dis.blit(IMG, IMG_POS)
    _pos_X, _pos_Y = FIRST_BOX_POS
    for j, col in enumerate(grid):
        pos_Y = _pos_Y + j*(BOX_H + 2*GAP)
        for i, num in enumerate(col):
            pos_X = _pos_X +i*(BOX_W + 2*GAP)
            fill_box(num, pos_X, pos_Y)


def show_score(score, color=FONT_COLOR):
    _score = text.render('Score : ' + str(int(score)), True, color)
    dis.blit(_score, (GAP, GAP))

    _newgame = text_opt.render('N - New Game', True, color)
    dis.blit(_newgame, pos_newgame)
    _exit = text_opt.render('E - Exit', True, color)
    dis.blit(_exit, pos_exit)


def show_game_over_message(score):
    dis.blit(surf, (0,0))
    mesg = text_go.render('GAME OVER', True, BLACK)
    pos = mesg.get_rect(center=(DIS_WIDTH/2, DIS_HEIGHT/2))
    dis.blit(mesg, pos)

    show_score(score, BLACK)


def show_win_message(score):
    dis.blit(surf, (0,0))
    mesg = text_go.render('YOU WIN', True, BLACK)
    pos = mesg.get_rect(center=(DIS_WIDTH/2, DIS_HEIGHT/2))
    dis.blit(mesg, pos)

    note = text_opt.render('Currently, the maximum value is reached.', True, BLACK)
    dis.blit(note, pos_note_first)
    note = text_opt.render('4096 will be added in a future version.', True, BLACK)
    dis.blit(note, pos_note_second)

    show_score(score, BLACK)




# SOUND EFFECTS
MERGED = pygame.mixer.Sound("files/sound/merge.mp3")
YOUWIN = pygame.mixer.Sound("files/sound/youwin.mp3")
GAMEOVER = pygame.mixer.Sound("files/sound/gameover.mp3")


def play_sound(is_merged, is_over, is_win):
    if is_win:
        pygame.mixer.Sound.play(YOUWIN)
    elif is_over:
        pygame.mixer.Sound.play(GAMEOVER)
    elif is_merged:
        pygame.mixer.Sound.play(MERGED)

    is_over, is_win, is_merged = False, False, False
