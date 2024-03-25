import sys
import random


"""
    BRICK GAME
    - Played between two players
    - Each player has 4 bricks in each round
    - Bricks are 5 cm x 10 cm (or short units x long units)
    - There will be a random distance between 250 cm and 500 cm between players
    - Each player moves in turn
    - WINNER is the one who leave their brick on the opponent's brick

    - 'l' stands for long and 's' stands for short
    - The distance remaining at each turn is displayed in [cm]
"""


# SET COLORS
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def game():
    global player1, player2
    player1, player2 = get_player_names()
    player_turn = who_starts_first()
    
    distance = decide_strating_distance()
    while distance >= 0:
        last_play = play_turn(player_turn)
        distance = distance_reducer(last_play, distance)
        if distance < 0:
            print(YELLOW + f"\n {player_turn.upper()} has WON! \n" + RESET)
            sys.exit()
        player_turn = change_turn(player_turn)


def get_player_names():
    while True:
        player1 = input("First player name: ").strip().title()
        player2 = input("Second player name: ").strip().title()
        if player1 != player2:
            return player1, player2
        print(RED + "Player names can't be same" + RESET)


def who_starts_first():
    player_turn = random.choice([player1, player2])
    print(f"{player_turn} will start")
    return player_turn


def decide_strating_distance():
    distance = random.randint(250, 500)
    print(YELLOW + f'First distance: {distance} cm' + RESET)
    return distance


def play_turn(player_turn):
    while True:
        move = input(f"{player_turn} make your move: ").lower()
        if len(move) != 4:
            print(RED + "You must play 4" + RESET)
            continue
        for char in move:
            if char not in 'ls':
                print(RED + "You can only play (l)ong or (s)hort" + RESET)
                break
        else:
            return move


def distance_reducer(last_play, distance):
    for char in last_play:
        if char == 'l':
            distance -= 10
        else:
            distance -= 5
    print(YELLOW + "Remaining distance: ", distance, " cm" + RESET)
    return distance


def change_turn(player_turn):
    return player1 if player_turn == player2 else player2


if __name__ == '__main__':
    game()
