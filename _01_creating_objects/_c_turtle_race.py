"""
Turtle Race
"""
import turtle
import random
from PIL import Image

# ================= Instructions at the bottom of this file ===================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))


def draw_background():
    filename = 'race_track.gif'

    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window = turtle.Screen()
    window.setup(image.width + 100, image.height + 100, startx=0, starty=0)
    window.bgpic(filename)
    window.onclick(screen_clicked)

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    draw_background()

    # TODO 1) Create an empty list of turtles
    turtle_list = []
    # TODO 2) Create a new turtle and set its shape to 'turtle

    # TODO 3) Set the turtle's speed to 3

    # TODO 4) Set the turtle's pen up

    # TODO 5) Use the turtle's goto() method to set its position on the left
    #  side of the screen

    # TODO 6) use a loop to repeat the previous instructions and create
    #  8 turtles lined up on the left side of the screen
    #  *HINT* click on the window to print the corresponding x, y location
    color_list = random.shuffle(['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'black', 'cyan'])
    for i in range(8):
        bob = turtle.Turtle()
        bob.shape('turtle')
        bob.speed(3)
        bob.penup()
        bob.setx(-418)
        bob.sety(190-i*55)
        bob.color(color_list[i])
        turtle_list.append(bob)

    # TODO 7) Move each turtle forward a random distance between 1 and 20

    # TODO 8) Create a loop to keep moving each turtle until a turtle
    #  crosses the finish line
    #  *HINT* click on the window to print the corresponding x, y location
    winner = None
    number = 0
    while winner is None:
        number = 0
        for t in turtle_list:
            number = number + 1
            t.forward(random.randint(1, 10))
            if t.xcor() > 350:
                winner = number
                break

    print("Turtle", number, "wins!")
    # TODO 9) When a turtle crosses the finish line, stop the race and
    #  indicate which turtle won the race

    # EXTRA: Create different colors for each turtle and code a special
    # dance for the winning turtle!

turtle.done()
