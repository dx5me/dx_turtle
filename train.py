import turtle

import random

random.seed(7)  # Same seed every run, so the stars land in the same places

zx = turtle.Screen()

dx = turtle.Turtle()

RAIL_Y = -16   # Storing rail level at one place so wheels and other parts sit on the same line
WHEEL_R = 14   # Radius of the big wheels, used to lift the train body above the rails


def setup_screen():
    zx.title("Train Project")
    zx.setup(800, 600)
    zx.bgcolor("#141a33")  # Dark blue background
    zx.tracer(0)  # Turn off automatic screen updates; we call zx.update() once at the end
    dx.speed(0)  # Fastest turtle speed
    dx.hideturtle()  # Hide the turtle cursor for a cleaner look


def draw_polygon(points, color):
    dx.pensize(1)
    dx.color(color)
    dx.penup()
    dx.goto(points[0])
    dx.pendown()
    dx.begin_fill()
    for point in points[1:]:
        dx.goto(point)
    dx.goto(points[0])  # Close the polygon
    dx.end_fill()
    dx.penup()  # Lift the pen to avoid drawing lines when moving to the next shape


def draw_rectangle(x, y, width, height, color):
    corners = [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]
    draw_polygon(corners, color)


def draw_circle(x, y, radius, color, outline_color=None):
    # Filled circle centred on (x, y); the outline is optional
    if outline_color is not None:
        dx.pensize(2)
        dx.color(outline_color, color)
    else:
        dx.pensize(1)
        dx.color(color)
    dx.penup()
    dx.setheading(0)  # Reset the heading to 0 degrees
    dx.goto(x, y - radius)  # Move to the bottom of the circle
    dx.pendown()
    dx.begin_fill()
    dx.circle(radius)
    dx.end_fill()
    dx.penup()  # Lift the pen to avoid drawing lines when moving to the next shape


def draw_line(x1, y1, x2, y2, color, width):
    dx.pensize(width)
    dx.color(color)
    dx.penup()
    dx.goto(x1, y1)
    dx.pendown()
    dx.goto(x2, y2)
    dx.penup()  # Lift the pen to avoid drawing lines when moving to the next shape


# ---------------- Sky ----------------

def draw_stars(count):
    for _ in range(count):
        x = random.randint(-400, 400)
        y = random.randint(60, 300)
        size = random.randint(2, 4)
        dx.penup()
        dx.goto(x, y)
        dx.dot(size, "#e6ecff")


def draw_moon(x, y, radius):
    draw_circle(x, y, radius, "#f3ecc8")  # The moon
    draw_circle(x - 13, y + 8, 6, "#e2d9ae")  # Craters
    draw_circle(x + 13, y - 12, 4, "#e2d9ae")
    draw_circle(x + 4, y + 14, 3, "#e2d9ae")


def draw_hills():
    draw_polygon([(-400, RAIL_Y), (-400, 40), (-300, 90), (-180, 50), (-60, 110),
                  (60, 60), (180, 100), (300, 45), (400, 80), (400, RAIL_Y)], "#1d2547")


# ---------------- Ground and track ----------------

def draw_ground():
    draw_rectangle(-400, -300, 800, 300 + RAIL_Y, "#1f3a2b")  # Grass
    draw_rectangle(-400, RAIL_Y - 22, 800, 18, "#3b3a3f")  # Gravel bed under the track


def draw_track():
    for x in range(-400, 400, 24):  # Wooden sleepers
        draw_rectangle(x, RAIL_Y - 16, 14, 10, "#5a3d2b")
    draw_line(-400, RAIL_Y - 2, 400, RAIL_Y - 2, "#b8bcc8", 3)  # Rail


# ---------------- Train ----------------

def draw_wheel(x, radius=WHEEL_R):
    y = RAIL_Y + radius  # Centre sits so the bottom of the wheel touches the rail
    draw_circle(x, y, radius, "#2b2b2b", "#c9c9c9")
    draw_circle(x, y, radius * 0.35, "#9a9a9a")  # Hub


def draw_window(x, y, w, h):
    draw_rectangle(x, y, w, h, "#ffd56b")  # Warm lit window
    draw_line(x + w / 2, y, x + w / 2, y + h, "#c99a2e", 1)


def draw_locomotive(x):
    base = RAIL_Y + WHEEL_R  # Body starts just above the wheel centres
    # Chassis
    draw_rectangle(x - 5, base - 4, 190, 10, "#1b1b1b")
    # Boiler (long body) and cab
    draw_rectangle(x, base + 6, 120, 46, "#b3262e")
    draw_rectangle(x + 120, base + 6, 60, 84, "#8e1d24")
    draw_rectangle(x + 114, base + 90, 72, 8, "#2b2b2b")  # Cab roof
    draw_window(x + 134, base + 50, 32, 26)
    # Gold stripe along the boiler
    draw_rectangle(x, base + 26, 120, 5, "#e0b341")
    # Chimney, dome and headlamp
    draw_rectangle(x + 18, base + 52, 20, 28, "#2b2b2b")
    draw_rectangle(x + 14, base + 80, 28, 7, "#2b2b2b")
    draw_circle(x + 72, base + 56, 10, "#e0b341")
    draw_circle(x - 4, base + 36, 7, "#fff3b0", "#2b2b2b")
    # Cow catcher at the front
    draw_polygon([(x - 5, base + 6), (x - 30, RAIL_Y + 2), (x - 5, RAIL_Y + 2)], "#555555")
    # Wheels and connecting rod
    for wx in (x + 25, x + 65, x + 105):
        draw_wheel(wx)
    draw_wheel(x + 155, 10)
    draw_line(x + 25, RAIL_Y + WHEEL_R, x + 105, RAIL_Y + WHEEL_R, "#c9c9c9", 3)
    # Smoke puffs drifting back from the chimney
    puffs = [(28, 98, 9), (12, 116, 12), (-12, 134, 15), (-42, 150, 18), (-80, 162, 21)]
    for px, py, r in puffs:
        draw_circle(x + px, base + py, r, "#8b90a6")


def draw_carriage(x, color):
    base = RAIL_Y + WHEEL_R
    draw_rectangle(x, base - 4, 150, 10, "#1b1b1b")  # Chassis
    draw_rectangle(x, base + 6, 150, 62, color)  # Body
    draw_rectangle(x - 4, base + 68, 158, 8, "#2b2b2b")  # Roof
    for wx in range(int(x) + 12, int(x) + 140, 34):
        draw_window(wx, base + 30, 24, 24)
    for wx in (x + 25, x + 125):
        draw_wheel(wx, 11)


def draw_coupler(x1, x2):
    y = RAIL_Y + WHEEL_R + 2
    draw_line(x1, y, x2, y, "#1b1b1b", 4)


def draw_train(x):
    draw_locomotive(x)
    draw_coupler(x + 185, x + 200)
    draw_carriage(x + 200, "#2f6db5")
    draw_coupler(x + 350, x + 365)
    draw_carriage(x + 365, "#2f8f5b")


# ---------------- Main ----------------

def main():
    setup_screen()
    draw_stars(56)
    draw_moon(276, 224, 32)
    draw_hills()
    draw_ground()
    draw_track()
    draw_train(-260)
    zx.update()  # Show everything we drew while tracer was off


main()
turtle.done()  # Keep the window open
