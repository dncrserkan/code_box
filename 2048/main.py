# import pygame
from visuals import *
from functions import *


WINNER = 2048


def listen_events(running, waiting, only_EN):
    dir = -1                                     # Avoid unbound variable error, loop will wait for keydown event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            waiting = False
        if event.type == pygame.KEYDOWN:
            waiting = False
            if event.key == pygame.K_e:
                running = False
            elif event.key == pygame.K_n:
                startGame()
                quit()
            elif not only_EN:
                if event.key == pygame.K_LEFT :
                    dir = 0
                elif event.key == pygame.K_RIGHT:
                    dir = 2
                elif event.key == pygame.K_UP:
                    dir = 1
                elif event.key == pygame.K_DOWN:
                    dir = 3
            else:                                           # In case other key press
                waiting = True
    return running, waiting, dir



def startGame():  
    grid = create_new_grid()
    move.score = 0 

    is_over, is_win, is_merged = False, False, False
    running = True
    while running:  
        last_grid = grid.copy()
        show_boxes(grid)
        show_score(move.score)
        pygame.display.update()


        only_EN = False                                     # Listen for only Exit-New Game
        if np.any(grid==WINNER):                            # Win check
            show_win_message(move.score)
            pygame.display.update()
            only_EN = True
            is_win = True
        

        if check_game_over(grid):
            show_game_over_message(move.score)
            pygame.display.update()
            only_EN = True
            is_over = True
        

        play_sound(is_merged, is_over, is_win)

        waiting = True
        while waiting:
            running, waiting, dir = listen_events(running, waiting, only_EN)
            
        
        if dir != -1:                                       # Do not work until dir is valid
            grid, is_merged = move(grid, dir)
        
        if not np.array_equal(grid, last_grid):             # If the grid changed add new number
            grid = addNumber(grid)



if __name__ == '__main__':
    startGame()
