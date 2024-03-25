import random


def main(function, times=1000):
    """
    function: which function will be use
    times: number of tries """
    score = 0
    for _ in range(times):
        door_list = distribute_options()
        selected_door = choose_the_door(door_list)
        get_rid_of_one_door(selected_door, door_list)
        if function(selected_door) == "Cash":
            score += 1

    perc_score = score / times * 100
    print(f"\tScore: {perc_score:.2f}")


def distribute_options():
    options = ["Cash", "Trash", "Garbage"]
    # No need to shuffle, but we do it anyway
    random.shuffle(options)
    return options


def choose_the_door(door_list):
    return random.choice(door_list)


def get_rid_of_one_door(selected_door, door_list):
    if selected_door == "Cash":
        will_be_delete = "Trash"
    elif selected_door == "Trash":
        will_be_delete = "Garbage"
    elif selected_door == "Garbage":
        will_be_delete = "Trash"
    door_list.remove(will_be_delete)


def change_the_door(selected_door):
    if selected_door == "Cash":
        return "Trash"
    else:
        return "Cash"


def do_not_change_the_door(selected_door):
    return selected_door


def randomly_change_the_door(prevent_error):
    return random.choice(["Cash", "Trash"])


if __name__ == "__main__":
    print('When we change the door each time')
    main(change_the_door, times=1_000_000)

    print('When we keep the door the same each time')
    main(do_not_change_the_door, times=1_000_000)

    print('When we randomly change the door each time')
    main(randomly_change_the_door, times=1_000_000)
