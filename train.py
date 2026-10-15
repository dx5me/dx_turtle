import turtle

import random

import math

zx = turtle.Screen()

dx = turtle.Turtle()

RAIL_Y = -16   #Storing Rail level at one level so wheels and other parts could be stored at same level

# The scene is designed on an 800 x 600 grid. On a bigger (or smaller) screen
# every coordinate is multiplied by SCALE, and HALF_W / HALF_H tell us how far
# the visible area reaches in design units, so the sky, cliffs and rails can
# stretch all the way to the screen edges.
DESIGN_W = 800
DESIGN_H = 600
SCALE = 1.0
HALF_W = DESIGN_W / 2
HALF_H = DESIGN_H / 2


def setup_screen():
    zx.title("Train Project")
    zx.setup(width=1.0, height=1.0)  # Window as big as the screen
    window = zx.getcanvas().winfo_toplevel()
    window.attributes("-fullscreen", True)  # True fullscreen, no title bar
    zx.bgcolor("#141a33") # Dark blue background
    # Remove turtle's sunken border and paint the gaps around the canvas the same blue
    zx.getcanvas().config(borderwidth=0, highlightthickness=0)
    zx.getcanvas().configure(bg="#141a33")
    window.configure(bg="#141a33")
    zx.tracer(0)  # Turn off automatic screen updates; zx.update() shows everything at the end
    dx.speed(0)  # Fastest turtle speed
    dx.hideturtle()  # Hide the turtle cursor for a cleaner look

    # Escape leaves fullscreen, F11 toggles it back
    window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))
    window.bind("<F11>", lambda event: window.attributes(
        "-fullscreen", not window.attributes("-fullscreen")))
    # Redraw whenever the window changes size ("+" keeps turtle's own resize handler)
    window.bind("<Configure>", on_resize, add="+")


def update_scale():
    global SCALE, HALF_W, HALF_H
    window = zx.getcanvas().winfo_toplevel()
    zx.screensize(1, 1)  # Shrink first so turtle hides any scrollbars it showed mid-resize
    window.update()
    width = max(window.winfo_width(), 200)
    height = max(window.winfo_height(), 150)
    # Fit the whole 800 x 600 design on screen without stretching it
    SCALE = min(width / DESIGN_W, height / DESIGN_H)
    HALF_W = width / 2 / SCALE
    HALF_H = height / 2 / SCALE
    zx.screensize(width - 4, height - 4)  # Scroll area just inside the window, so turtle hides its scrollbars


def pos(x, y):
    # Convert a design coordinate to a screen coordinate
    return (x * SCALE, y * SCALE)


def draw_polygon(points, color):
    dx.pensize(1)
    dx.color(color)
    dx.penup()
    dx.goto(pos(*points[0]))
    dx.pendown()
    dx.begin_fill()
    for point in points[1:]:
        dx.goto(pos(*point))
    dx.goto(pos(*points[0]))  # Close the polygon
    dx.end_fill()
    dx.penup()  # Lift the pen to avoid drawing lines when moving to the next shape

def draw_rectangle(x, y, width, height, color):
    # (x, y) is the TOP-left corner; the rectangle grows down by `height`
    corners = [(x, y), (x + width, y), (x + width, y - height), (x, y - height)]
    draw_polygon(corners, color)

def draw_circle(x, y, radius, color, outline_color=None):
    if outline_color is not None:
        dx.pensize(max(1, 2 * SCALE))
        dx.color(outline_color, color)  # Pen colour for the outline, fill colour inside
    else:
        dx.pensize(1)
        dx.color(color)
    dx.penup()
    dx.setheading(0)  # Reset the heading to 0 degrees
    dx.goto(pos(x, y - radius))  # Move to the starting point of the circle
    dx.pendown()
    dx.begin_fill()
    dx.circle(radius * SCALE)
    dx.end_fill()
    dx.penup()  # Lift the pen to avoid drawing lines when moving to the next shape


def draw_line(x1, y1, x2, y2, color, width):
    dx.pensize(max(1, width * SCALE))
    dx.color(color)
    dx.penup()
    dx.goto(pos(x1, y1))
    dx.pendown()
    dx.goto(pos(x2, y2))
    dx.penup()  # Lift the pen to avoid drawing lines when moving to the next shape


def draw_stars(count):
    for _ in range(count):
        x = random.randint(int(-HALF_W), int(HALF_W))
        y = random.randint(100, int(HALF_H))
        size = random.randint(2, 4)
        dx.penup()
        dx.goto(pos(x, y))
        dx.dot(max(1, size * SCALE), "#e6ecff")


def draw_moon(x, y, radius):
    draw_circle(x, y, radius, "#f3ecc8")  # Draw the moon
    draw_circle(x - 13, y + 8, 6, "#e2d9ae")  # Craters
    draw_circle(x + 13, y - 12, 4, "#e2d9ae")


def draw_mountains():
    points = [(-HALF_W, 20), (-316, 76), (-211, 44), (-106, 116), (20, 52),
              (125, 104), (251, 64), (HALF_W, 112), (HALF_W, -32), (-HALF_W, -32)]

    draw_polygon(points, "#1d2442")  # Darker shade for mountains


def draw_canyon_back():
    draw_rectangle(-106, -20, 294, HALF_H - 20, "#10142a")


def draw_river():
    draw_polygon([(-85, -292), (159, -284), (159, -HALF_H), (-85, -HALF_H)], "#2c4a74")
    draw_line(-68, -300, 12, -298, "#4f75a6", 2)
    draw_line(49, -304, 129, -302, "#4f75a6", 2)


def draw_headlight_beam():
    light = (-119, 40)
    # The beam spreads by the same angle however far right the screen goes
    reach = (HALF_W + 119) / 519
    draw_polygon([light, (HALF_W, 40 + 110 * reach), (HALF_W, 40 - 130 * reach)], "#232a48")
    draw_polygon([light, (HALF_W, 40 + 75 * reach), (HALF_W, 40 - 95 * reach)], "#2f3656")
    draw_polygon([light, (HALF_W, 40 + 42 * reach), (HALF_W, 40 - 62 * reach)], "#40445f")
    draw_polygon([light, (HALF_W, 40 + 12 * reach), (HALF_W, 40 - 32 * reach)], "#6b6955")


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
    draw_polygon([(-HALF_W, -24), (-85, -24), (-70, -80), (-89, -160),
                  (-62, -252), (-85, -HALF_H), (-HALF_W, -HALF_H)], "#4a3a35")
    # Right cliff: slightly darker, as if it's more in shadow.
    draw_polygon([(HALF_W, -24), (163, -24), (150, -92), (173, -180),
                  (142, -260), (159, -HALF_H), (HALF_W, -HALF_H)], "#433430")


def draw_rock_layers():

    for y in range(-72, int(-HALF_H), -36):
        # Left cliff layer, tilted 4 pixels so it doesn't look ruler-straight.
        draw_line(-HALF_W, y, -100, y - 4, "#3a2d29", 3)
        # Right cliff layer, tilted the opposite way.
        draw_line(178, y + 4, HALF_W, y, "#352824", 3)


def draw_grass():
    # Thin dark grass strip on top of the left cliff.
    draw_rectangle(-HALF_W, -20, HALF_W - 85, 8, "#2f3a2c")
    # Same on the right cliff.
    draw_rectangle(163, -20, HALF_W - 163, 8, "#2f3a2c")


def draw_bridge_deck():
    draw_polygon([(-85, -20), (24, -20), (16, -26), (26, -32), (-85, -32)], "#5a4636")
    draw_polygon([(100, -20), (167, -20), (167, -32), (106, -32), (96, -26)], "#5a4636")


def draw_tracks():
    # Step back from -392 in 19s so the ties keep the same spacing on wide screens
    first_tie = -392 - 19 * math.ceil((HALF_W - 392) / 19)
    for x in range(first_tie, 20, 19):
        # Each tie is a short thick dash.
        draw_line(x, -20, x + 8, -20, "#2a201b", 4)

    for x in range(104, int(HALF_W), 19):
        draw_line(x, -20, x + 8, -20, "#2a201b", 4)
    draw_line(-HALF_W, RAIL_Y, 26, RAIL_Y, "#9aa0aa", 3)  # Left rail, up to the break
    draw_line(98, RAIL_Y, HALF_W, RAIL_Y, "#9aa0aa", 3)   # Right rail, after the break


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


def draw_scene():
    random.seed(7)  # Same stars, fog and debris on every redraw
    update_scale()
    dx.clear()
    # Back to front: sky, then canyon, then the bridge, then cliffs, then the train on top
    draw_stars(int(40 * HALF_W / 400))  # More stars on wider screens
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


last_size = None
pending_redraw = None

def on_resize(event):
    global last_size, pending_redraw
    size = (event.width, event.height)
    if event.widget is not zx.getcanvas().winfo_toplevel() or size == last_size:
        return
    last_size = size
    # Wait until the user stops dragging the window edge, then redraw once
    window = zx.getcanvas().winfo_toplevel()
    if pending_redraw is not None:
        window.after_cancel(pending_redraw)
    pending_redraw = window.after(150, draw_scene)


def main():
    setup_screen()  # Must run first so the window size and background are set before drawing
    draw_scene()


main()
turtle.done()
