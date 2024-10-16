############################################################
# Name:sonora
# Name(s) of anyone worked with:
# Est time spent (hr):
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!
# Draw the flower center
    center = GOval(WIDTH // 4, HEIGHT // 4)
    center.set_filled(True)
    center.set_fill_color("yellow")
    center.set_location(WIDTH // 2 - center.get_width() // 2, HEIGHT // 2 - center.get_height() // 2)
    gw.add(center)
    

    # Draw petals
    petal_size = (WIDTH // 5, HEIGHT // 10)
    petal_positions = [
        (WIDTH // 2 - petal_size[0] // 2, HEIGHT // 2 - petal_size[1] // 2 - 75),  # Top petal
        (WIDTH // 2 - petal_size[0] // 2, HEIGHT // 2 + petal_size[1] // 2 + 30),  # Bottom petal
        (WIDTH // 2 - petal_size[0] - 40, HEIGHT // 2 - petal_size[1] // 2),      # Left petal
        (WIDTH // 2 + petal_size[0] - 60, HEIGHT // 2 - petal_size[1] // 2),      # Right petal
        (WIDTH // 2 - petal_size[0] // 2 - 55, HEIGHT // 2 - petal_size[1] // 2 - 40),  # Top-left petal
        (WIDTH // 2 + petal_size[0] // 2 - 35, HEIGHT // 2 - petal_size[1] // 2 - 40),  # Top-right petal
        (WIDTH // 2 - petal_size[0] // 2 - 70, HEIGHT // 2 + petal_size[1] // 2 - 5),  # Bottom-left petal
        (WIDTH // 2 + petal_size[0] // 2 - 30, HEIGHT // 2 + petal_size[1] // 2 - 5)   # Bottom-right petal
    ]

    for pos in petal_positions:
        petal = GOval(petal_size[0], petal_size[1])
        petal.set_filled(True)
        petal.set_fill_color("pink")
        petal.set_location(pos[0], pos[1])
        gw.add(petal)






if __name__ == '__main__':
    draw_image()
