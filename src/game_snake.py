from graphics import *
import time
import math
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
GRID_SIZE = 20  # Size of each grid block
DELAY = 0.1

def create_black_square(canvas):
    # Calculate random position aligned with the grid
    x_l = random.randint(0, (CANVAS_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    y_t = random.randint(0, (CANVAS_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    x_r = x_l + GRID_SIZE
    y_b = y_t + GRID_SIZE
    square_rand = Rectangle(Point(x_l, y_t), Point(x_r, y_b))
    square_rand.setFill("black")
    square_rand.draw(canvas)
    return square_rand, x_l, y_t

def main():
    canvas = GraphWin("canvas", CANVAS_WIDTH, CANVAS_HEIGHT)

    # Initial position of the green square, aligned with the grid
    start_x = CANVAS_WIDTH // 2 - (CANVAS_WIDTH // 2 % GRID_SIZE)
    start_y = CANVAS_HEIGHT // 2 - (CANVAS_HEIGHT // 2 % GRID_SIZE)

    # Create the green square
    square = Rectangle(Point(start_x, start_y), Point(start_x + GRID_SIZE, start_y + GRID_SIZE))
    square.setFill("green")
    square.draw(canvas)

    # Create the initial black square
    black_square, black_x, black_y = create_black_square(canvas)

    # Initial direction (moving to the right)
    direction_x, direction_y = 1, 0

    while True:
        # Calculate new position based on current direction
        new_x = start_x + direction_x * GRID_SIZE
        new_y = start_y + direction_y * GRID_SIZE

        # Check boundaries to ensure the square stays within the canvas
        if 0 <= new_x and new_x + GRID_SIZE <= CANVAS_WIDTH and 0 <= new_y and new_y + GRID_SIZE <= CANVAS_HEIGHT:
            square.move(direction_x * GRID_SIZE, direction_y * GRID_SIZE)
            start_x = new_x
            start_y = new_y
        else:
            # If the square hits the boundary, stop moving in that direction
            direction_x = 0
            direction_y = 0

        # Check if the green square reaches the black square
        if start_x == black_x and start_y == black_y:
            black_square.undraw()  # Delete the black square
            black_square, black_x, black_y = create_black_square(canvas)  # Create a new black square at a random position

        # Check for mouse clicks to update direction
        click_point = canvas.checkMouse()
        if click_point:
            x, y = click_point.getX(), click_point.getY()
            print(f'Clicked at ({x}, {y})')

            # Calculate the center of the square
            square_center_x = start_x + GRID_SIZE / 2
            square_center_y = start_y + GRID_SIZE / 2

            # Calculate the direction vector
            direction_x = x - square_center_x
            direction_y = y - square_center_y

            # Normalize the direction vector and convert to grid steps
            length = math.sqrt(direction_x ** 2 + direction_y ** 2)
            if length > 0:
                direction_x = direction_x / length
                direction_y = direction_y / length

            # Convert direction to grid steps
            if abs(direction_x) > abs(direction_y):
                direction_x = 1 if direction_x > 0 else -1
                direction_y = 0
            else:
                direction_x = 0
                direction_y = 1 if direction_y > 0 else -1

        time.sleep(DELAY)

if __name__ == '__main__':
    main()
