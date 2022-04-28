import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro1():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a dragon "
                "is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your "
                f"rusty dagger.\n")


def intro2():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")


def intro():
    intro1()
    intro2()


# validates user input.
def valid_input(prompt, option1, option2):
    while True:
        response = (input(prompt))
        if str(option1) == response:
            break
        elif str(option2) == response:
            break
    return response