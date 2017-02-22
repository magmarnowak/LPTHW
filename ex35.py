from sys import exit

def start():
    print """
    You are in the dark room.
    There is a door to your right and left.
    Which one do you take?
    """
    choice = raw_input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else: dead("You stumble around the room until you starve.")

def dead(why):
    print why, "Good job!"
    exit(0)

def bear_room():
    print """
    There is a bear here.
    The bear has a bunch fo honey.
    The fat bear is in front of another door.
    How are you going to move the bear?"""
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print """
    Here you see the great evil Chthulu.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or eat your head?
    """

    choice = raw_input("> ")

    if "flee" in choice:
        start() #what is happening here?
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")

    if "0" in choice or "1" in choice: #improve this
        how_much = int(choice)

    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0) #what does it do? why not break? indicates to abort the program
        #without error, exit(1) would indicate an exit with an error
    else:
        dead("You greedy bastard!")

start()
