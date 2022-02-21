import turtle


def balra():
    pass


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("background.png")
space.addshape("sprite.gif")
space.onkeypress(balra, "Left")


ship = turtle.Turtle()
ship.shape("sprite.gif")

while True:
    space.update()
