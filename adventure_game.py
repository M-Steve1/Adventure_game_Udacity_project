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


def field():
    response = valid_input("What would you like to do?\n"
                           "(Please enter 1 or 2.)\n", 1, 2)
    if str(1) == response:
        print_pause("what happens in the house")
        house()
    elif str(2) == response:
        print_pause("what happens in the cave")
        cave()


def lose_fight():
    print_pause("You do your best...")
    print_pause(f"but your rusty dagger is no match for "
                f"the dragon.")
    print_pause("You have been defeated!")
    # play_again function goes here


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause(f"You have found the sword.")
    print_pause(f"You discard your rusty dagger and take"
                f"the sword with you.")
    print_pause("You walk back out to the field.")

    x = 0
    while x < 2:
        intro2()

        cave_response = valid_input("What would you like to do "
                                    "(Please enter 1 or 2.)\n", 1, 2)

        if str(1) == cave_response:
            house_scenerio()
            response = valid_input("Would you like to"
                                   "(1) fight or (2) run away?", 1, 2)
            if str(1) == response:
                print_pause("you win")
                x = 3
            elif str(2) == response:
                print_pause("You run back into the field. Luckily, "
                            "you don't seem to have been followed.\n")

        elif str(2) == cave_response:
            print_pause("You peer cautiously into the cave.")
            print_pause("You've been here before, "
                        "and gotten all the good stuff.")
            print_pause("It's just an empty cave now.")
            print_pause("You walk back out to the field.")


def house_scenerio():
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door "
                f"opens and out steps a dragon")
    print_pause(f"Eep! This is the dragon house!")
    print_pause(f"The dragon attacks you!")


def house():
    house_scenerio()
    print_pause(f"You feel a bit under-prepared for this,"
                f"what with only having a rusty dagger.")
    house_response = valid_input("Would you like to"
                                 "(1) fight or (2) run away?", 1, 2)
    if str(1) == house_response:
        lose_fight()
        print_pause("you lost")
    elif str(2) == house_response:
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
    else:
        print_pause("(Please enter 1 or 2.)")


intro()
field()