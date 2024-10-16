########################################
# Name: sonora
# Collaborators:
# Estimated time spent (hrs):
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)

    # You got it from here
win_width = BRICK_WIDTH * BRICKS_IN_BASE
    win_height = BRICK_HEIGHT * (BRICKS_IN_BASE + 1) // 2
    start_x = (win_width // 2) - (BRICK_WIDTH // 2)
    start_y = win_height - (BRICK_HEIGHT // 2)
    
    for row in range(BRICKS_IN_BASE):
        num_bricks = BRICKS_IN_BASE - row
        y_position = start_y - (row * BRICK_HEIGHT)

        x_start = start_x - (row * (BRICK_WIDTH // 2))
        
        for brick in range(num_bricks):
            x_position = x_start + (brick * BRICK_WIDTH)
            brick_rect = GRect(x_position, y_position, BRICK_WIDTH, BRICK_HEIGHT)
            gw.add(brick_rect)




if __name__ == '__main__':
    draw_pyramid()
