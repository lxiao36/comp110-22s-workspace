"""Real renaissance painting of three houses in a forest before they invented lawn mowers."""

__author__ = "730526509"

from turtle import Turtle, colormode, done
from random import randint 
bod: Turtle = Turtle()
rof: Turtle = Turtle()
win: Turtle = Turtle()
gra: Turtle = Turtle()


def main() -> None:
    """The point where all the components of the house is put together."""
    """The houses are duplicated and spread apart."""
    x = -300
    # x is set to -300 so the drawing starts further left of screen for more space
    y = 0
    i = 0 
    grass_length = 20
    side_length = 150
    while i < 3:
        win.penup()
        win.goto(x, y)
        win.pendown()
        body(roof(window(side_length, x, y), x, y), x, y)
        i += 1
        x += 200
        # here x is added by 200 for space between each house
    grass(grass_length)
    win.hideturtle()
    rof.hideturtle()
    bod.hideturtle()
    gra.hideturtle()


def window(sl: int, x: int, y: int) -> int:
    """The window of the house."""
    sl = sl // 6
    # By dividing sl (side length) by 6 the square becomes a smaller window size
    i = 0
    win.color("blue", "blue")
    win.begin_fill()
    win.penup()
    win.goto(x, y)
    win.pendown()
    win.speed(100)
    while (i < 4):
        win.forward(sl)
        win.left(90)
        i = i + 1
    win.end_fill()
    return sl


def roof(sl: int, x: int, y: int) -> int:
    """The roof of the house."""
    x -= 20 
    y += 110
    # x and y is changed so it is placed in the needed spot to form the house
    i = 0
    sl = 150
    # sl (side length) set back to 150 
    rof.color("red", "red")
    rof.begin_fill()
    rof.penup()
    rof.goto(x, y)
    rof.pendown()
    rof.speed(100)
    while (i < 3):
        rof.forward(sl)
        rof.left(120)
        i = i + 1
    rof.end_fill()
    return sl


def body(sl: int, x: int, y: int) -> int:
    """The body of the house."""
    y -= 40
    x -= 20
    # x and y is changed so it is placed in the needed spot to form the house
    i = 0
    bod.penup()
    bod.goto(x, y)
    bod.pendown()
    bod.speed(100)
    while (i < 4):
        bod.forward(sl)
        bod.left(90)
        i = i + 1
    return sl


def grass(tall: int) -> int:
    """Randomly placed grass."""
    i = 0 
    gra.pencolor("green")
    gra.left(90)
    # gra.left(90) turns line vertically
    gra.speed(100)
    while (i < 100):
        x: int = randint(-400, 300)
        # The while loop randomly chosed a x vaule from -400 to 300 one hundred times to place grass
        gra.penup()
        gra.goto(x, -40)
        gra.pendown()
        gra.forward(tall)
        i += 1
    return tall


if __name__ == "__main__":
    main()


done()