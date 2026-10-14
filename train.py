import turtle

import random

import math

random.seed(7)

zx = turtle.Screen()

dx = turtle.Turtle()

RAIL_Y = -16   #Storing Rail level at one level so wheels and other parts could be stored at same level

def setup_screen():
    zx.title("Train Project")
    zx.setup(800, 600)
    zx.bgcolor("#141a33") # Dark blue background
    zx.tracer(0)  # Turn off automatic screen updates; zx.update() shows everything at the end
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
    # (x, y) is the TOP-left corner; the rectangle grows down by `height`
    corners = [(x, y), (x + width, y), (x + width, y - height), (x, y - height)]
    draw_polygon(corners, color)

def draw_circle(x, y, radius, color, outline_color=None):
    if outline_color is not None:
        dx.pensize(2)
        dx.color(outline_color, color)  # Pen colour for the outline, fill colour inside
    else:
        dx.pensize(1)
        dx.color(color)
    dx.penup()
    dx.setheading(0)  # Reset the heading to 0 degrees
    dx.goto(x, y - radius)  # Move to the starting point of the circle
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


def draw_stars(count):
    for _ in range(count):
        x = random.randint(-400, 400)
        y = random.randint(100, 300)
        size = random.randint(2, 4)
        dx.penup()
        dx.goto(x, y)
        dx.dot(size, "#e6ecff")


def draw_moon(x, y, radius):
    draw_circle(x, y, radius, "#f3ecc8")  # Draw the moon
    draw_circle(x - 13, y + 8, 6, "#e2d9ae")  # Craters
    draw_circle(x + 13, y - 12, 4, "#e2d9ae")


def draw_mountains():
    points = [(-400, 20), (-316, 76), (-211, 44), (-106, 116), (20, 52),
              (125, 104), (251, 64), (400, 112), (400, -32), (-400, -32)]

    draw_polygon(points, "#1d2442")  # Darker shade for mountains


def draw_canyon_back():
    draw_rectangle(-106, -20, 294, 300, "#10142a")


def draw_river():
    draw_polygon([(-85, -292), (159, -284), (159, -320), (-85, -320)], "#2c4a74")
    draw_line(-68, -300, 12, -298, "#4f75a6", 2)
    draw_line(49, -304, 129, -302, "#4f75a6", 2)


def draw_headlight_beam():
    light = (-119, 40)
    draw_polygon([light, (400, 150), (400, -90)], "#232a48")
    draw_polygon([light, (400, 115), (400, -55)], "#2f3656")
    draw_polygon([light, (400, 82), (400, -22)], "#40445f")
    draw_polygon([light, (400, 52), (400, 8)], "#6b6955")


def draw_bridge_supports():
    for x in [-51, -9, 129]:
        draw_rectangle(x, -32, 10, 260, "#3d3029")
    braces = [
        (-41, -40, -9, -140),
        (-9, -40, -41, -140),
        (-41, -144, -9, -244),
        (-9, -144, -41, -244),
        (1, -40, 26, -88),
        (1, -92, 18, -152),
        (104, -44, 129, -128),
        (140, -40, 163, -128),
    ]

    for x1, y1, x2, y2 in braces:

        draw_line(x1, y1, x2, y2, "#3d3029", 4)


def draw_fog_row(start_x, base_y, count, spacing, color):

    for i in range(count):

        x = start_x + i * spacing + random.randint(0, 12)

        y = base_y - random.randint(0, 16)

        radius = random.randint(28, 40)

        draw_circle(x, y, radius, color)


def draw_debris():
    pieces = [(54, -132, 12), (70, -180, 10), (39, -204, 8),
              (83, -232, 7), (60, -264, 6), (96, -160, 6)]
    for cx, cy, size in pieces:
        start_angle = random.uniform(0, 2 * math.pi)
        corners = []
        for corner in range(4):
            angle = start_angle + corner * math.pi / 2 + random.uniform(-0.3, 0.3)
            px = cx + math.cos(angle) * size
            py = cy + math.sin(angle) * size * 0.6
            corners.append((px, py))
        draw_polygon(corners, "#6a5240")


def draw_broken_rails():
    draw_line(26, -18, 37, -64, "#9aa0aa", 3)
    draw_line(37, -64, 47, -108, "#9aa0aa", 3)
    draw_line(98, -18, 89, -56, "#9aa0aa", 3)


def draw_cliffs():
    # Left cliff: jagged right edge facing the canyon.
    draw_polygon([(-400, -24), (-85, -24), (-70, -80), (-89, -160),
                  (-62, -252), (-85, -320), (-400, -320)], "#4a3a35")
    # Right cliff: slightly darker, as if it's more in shadow.
    draw_polygon([(400, -24), (163, -24), (150, -92), (173, -180),
                  (142, -260), (159, -320), (400, -320)], "#433430")


def draw_rock_layers():

    for y in range(-72, -320, -36):
        # Left cliff layer, tilted 4 pixels so it doesn't look ruler-straight.
        draw_line(-400, y, -100, y - 4, "#3a2d29", 3)
        # Right cliff layer, tilted the opposite way.
        draw_line(178, y + 4, 400, y, "#352824", 3)


def draw_grass():
    # Thin dark grass strip on top of the left cliff.
    draw_rectangle(-400, -20, 315, 8, "#2f3a2c")
    # Same on the right cliff.
    draw_rectangle(163, -20, 237, 8, "#2f3a2c")


def draw_bridge_deck():
    draw_polygon([(-85, -20), (24, -20), (16, -26), (26, -32), (-85, -32)], "#5a4636")
    draw_polygon([(100, -20), (167, -20), (167, -32), (106, -32), (96, -26)], "#5a4636")


def draw_tracks():

    for x in range(-392, 20, 19):
        # Each tie is a short thick dash.
        draw_line(x, -20, x + 8, -20, "#2a201b", 4)

    for x in range(104, 400, 19):
        draw_line(x, -20, x + 8, -20, "#2a201b", 4)
    draw_line(-400, RAIL_Y, 26, RAIL_Y, "#9aa0aa", 3)  # Left rail, up to the break
    draw_line(98, RAIL_Y, 400, RAIL_Y, "#9aa0aa", 3)   # Right rail, after the break


def draw_signal_lamp():
    draw_line(7, RAIL_Y, 7, 26, "#8a8f99", 3)
    draw_circle(7, 32, 8, "#e24b4a")
    draw_circle(7, 32, 3, "#ffb3a8")


def draw_smoke():
    puffs = [(-366, 144, 24, "#454c6c"), (-316, 140, 24, "#454c6c"),
             (-266, 136, 22, "#454c6c"), (-219, 128, 20, "#454c6c"),
             (-182, 116, 16, "#5a6180"), (-152, 100, 12, "#5a6180")]
    for x, y, radius, color in puffs:

        draw_circle(x, y, radius, color)


def draw_speed_lines():
    draw_line(-400, 60, -380, 60, "#5a6180", 2)
    draw_line(-400, 72, -372, 72, "#5a6180", 2)


def draw_wheel(x, radius):
    y = RAIL_Y + radius
    draw_circle(x, y, radius, "#1a1b22", "#8a8f99")


def draw_passenger_car():
    draw_rectangle(-383, 48, 117, 52, "#33384a")
    for x in [-366, -333, -299]:
        draw_rectangle(x, 36, 19, 16, "#ffd66b")
    for x in [-362, -316, -282]:
        draw_wheel(x, 9)
    draw_line(-266, 8, -253, 8, "#8a8f99", 4)


def draw_locomotive():
    # Cab: the tall back part where the driver sits.
    draw_rectangle(-253, 84, 46, 88, "#2a2d38")
    # Cab window, lit yellow.
    draw_rectangle(-240, 72, 21, 20, "#ffd66b")
    # Cab roof, slightly wider than the cab, so it overhangs.
    draw_rectangle(-261, 92, 63, 10, "#1f2129")
    # Boiler: the long front body of the engine.
    draw_rectangle(-207, 56, 76, 60, "#2a2d38")
    # A lighter trim strip along the top of the boiler.
    draw_rectangle(-207, 62, 76, 6, "#3d4150")
    # Smokestack (chimney).
    draw_rectangle(-165, 84, 17, 28, "#1f2129")
    # Chimney cap, slightly wider than the stack.
    draw_rectangle(-169, 88, 25, 6, "#1f2129")
    # Cowcatcher: the slanted triangle at the front bottom.
    draw_polygon([(-131, 4), (-106, -16), (-131, -16)], "#6b6f7a")
    # Big wheels under the engine.
    for x in [-232, -194, -156]:
        # Radius 12: bigger than carriage wheels.
        draw_wheel(x, 12)
    # Connecting rod joining the wheel centres.
    draw_line(-232, RAIL_Y + 12, -156, RAIL_Y + 12, "#8a8f99", 3)
    # Headlight, outer glow.
    draw_circle(-127, 40, 11, "#fff6c8")
    # Headlight, bright white centre.
    draw_circle(-127, 40, 5, "#ffffff")


def main():
    setup_screen()  # Must run first so the window size and background are set before drawing
    # Back to front: sky, then canyon, then the bridge, then cliffs, then the train on top
    draw_stars(40)
    draw_moon(276, 224, 32)
    draw_mountains()
    draw_canyon_back()
    draw_river()
    draw_headlight_beam()
    draw_bridge_supports()
    draw_fog_row(-106, -152, 9, 36, "#2f3858")
    draw_debris()
    draw_broken_rails()
    draw_fog_row(-119, -204, 10, 34, "#3c4668")
    draw_cliffs()
    draw_rock_layers()
    draw_grass()
    draw_bridge_deck()
    draw_tracks()
    draw_signal_lamp()
    draw_smoke()
    draw_speed_lines()
    draw_passenger_car()
    draw_locomotive()
    zx.update()  # Show everything we drew while tracer was off


main()
turtle.done()
