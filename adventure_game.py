import time
import random


def enemy_randomness():
    villian_list = ["dragon", "pirate", "vampire", "wolf"]
    enemy_randomness.enemy = random.choice(villian_list)


def lethal_weapon():
    strong_weapon_list = ["magical Sword of Ogoroth", "magical Hammer",
                          "magical Spell Book"]
    lethal_weapon.strong_weapon = random.choice(strong_weapon_list)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro1():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy_randomness.enemy} "
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
                f"the {enemy_randomness.enemy}.")
    print_pause("You have been defeated!")
    play_again()


def win_fight():
    print_pause(f"As the {enemy_randomness.enemy} moves to attack, "
                f"you unsheath your new {lethal_weapon.strong_weapon}.")
    print_pause(f"The {lethal_weapon.strong_weapon} shines brightly in your "
                "hand as you brace yourself for the attack.")
    print_pause(f"But the {enemy_randomness.enemy} takes one look at your "
                "shiny new toy and runs away!")
    print_pause(f"You have rid the town of the {enemy_randomness.enemy}. "
                "You are victorious!")
    play_again()


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause(f"You have found the {lethal_weapon.strong_weapon}.")
    print_pause(f"You discard your rusty dagger and take"
                f"the {lethal_weapon.strong_weapon} with you.")
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
                win_fight()
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
                f"opens and out steps a {enemy_randomness.enemy} ")
    print_pause(f"Eep! This is the {enemy_randomness.enemy} house!")
    print_pause(f"The {enemy_randomness.enemy} attacks you!")


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


def play_again():
    play_again_response = valid_input("Would you like to play again? (y/n)",
                                      "y", "n")
    if "y" == play_again_response:
        print_pause("Excellent! Restarting the game ...\n")
        # call play_game funtion here 
    elif "n" == play_again_response:
        print_pause("Thanks for playing! See you next time.")
    else:
        print_pause("Would you like to play again? (y/n)")


intro()
field()