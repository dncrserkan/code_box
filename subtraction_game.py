import random
import sys


""" 
Whoever says 0 is loses
You can only subtract 1 or 2
"""

# SET COLORS
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def game(smart):
    player_turn = who_is_first()
    _number = random.randint(20,60)
    print("First number:", _number)
    print("- " * 15)

    while _number > 0:
        if player_turn == 'computer':
            _number = comp_turn_play(_number, smart)
        else:
            _number = user_turn_play(_number)

        player_turn = change_turn(player_turn)
        if check_for_winner(_number, player_turn):
            sys.exit()


def who_is_first():
    while True:
        player_turn = input("select who play first 'computer' or 'player' or 'random' ").lower()
        if player_turn == "random":
            player_turn = random.choice(["computer", "player"])
        elif player_turn not in ["computer", "player"]:
            print("Select who play first!")
            continue

        print(f"{player_turn} play first")
        return player_turn


def comp_turn_play(_number, smart):
    if _number == 1:
        print(GREEN + '\nThe computer can only choose 1' + RESET)
        comp_choose = 1
    elif smart and _number % 3 == 0:
        comp_choose = 2
    elif smart and _number % 3 == 2:
        comp_choose = 1
    else:        
        comp_choose = random.choice([1, 2])

    print(GREEN + f"Computer choose: -{comp_choose}\t and say: {_number - comp_choose}" + RESET)
    return _number - comp_choose


def user_turn_play(_number):
    while True:
        if _number == 1:
            print(YELLOW + '\nYou can only choose 1' + RESET)
            users_choose = 1
            break
            
        users_choose = input('\n subtract 1 or 2: ')
        if users_choose in ['1', '2']:
            users_choose = int(users_choose)
            break
        else:
            print(RED + "You can only subtract 1 or 2!" + RESET)

    print(YELLOW + f"Player choose: -{users_choose} \t and say: {_number - users_choose}" + RESET)
    return _number - users_choose


def change_turn(player_turn):
    if player_turn == "computer":
        return "player"
    return "computer"


def check_for_winner(_number, player_turn):
    if _number == 0:
        print(RED + f"\n{(player_turn).upper()} has WON!\n" + RESET)
        return True


if __name__ == '__main__':
    game(smart=True)
