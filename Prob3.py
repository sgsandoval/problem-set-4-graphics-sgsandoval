########################################
# Name:
# Collaborators:
# Estimate time spent (hrs):
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():

    def on_mouse_down(event, square, score_label):
    global score 
    
        # Check if the click is within the square
        if (square.get_x() <= event.get_x() <= square.get_x() + SQUARE_SIZE and
            square.get_y() <= event.get_y() <= square.get_y() + SQUARE_SIZE):
        # Move square to a new random position
            new_x = random.randint(0, WIDTH - SQUARE_SIZE)
            new_y = random.randint(0, HEIGHT - SQUARE_SIZE)
            square.set_location(new_x, new_y)

            score += 1
        else:
            score = 0
    
    score_label.set_text(f"Score: {score}") 
    square = GRect(SQUARE_SIZE, SQUARE_SIZE)
    square.set_filled(True)
    square.set_fill_color("green")
    square.set_location((WIDTH - SQUARE_SIZE) // 2, (HEIGHT - SQUARE_SIZE) // 2)
    gw.add(square)
    
    # Score tracking
    score = 0
    score_label = GLabel(f"Score: {score}")
    score_label.set_location(SCORE_DX, HEIGHT - SCORE_DY) 
    gw.add(score_label)

    # Mouse click listener
    gw.add_event_listener("click", on_mouse_down())

   # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function

    gw = GWindow(GW_WIDTH, GW_HEIGHT)












if __name__ == '__main__':
    clicky_box()
