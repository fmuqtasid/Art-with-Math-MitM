# bubbles.py
# This program demonstrates an example of a fractal drawing using recursion and
# the picture module.

import picture

# This function recursively draws bubbles on a canvas
#
# Parameters:
# x: the x-coordinate of the center of the new bubble
# y: the y-coordinate of the center of the new bubble
# r: the radius of the new bubble to draw
# depth: the current depth of recursion

def bubbles(x, y, r, depth):
    """
    Recursively draws a pattern of circles resembling a bubble fractal.

    Inputs:
        x: The x-coordinate of the center of the current circle.
        y: The y-coordinate of the center of the current circle.
        r: The radius of the current circle.
        depth: The number of recursive levels to draw. Stops when depth reaches 0.

    Outputs:
        None
    """
    if depth > 0:
        # draw the primary circle
        picture.draw_filled_circle(x, y, r)

        # recursively draw another pattern in the top left (northwest)
        northwest_x = x - r
        northwest_y = y - r
        bubbles(northwest_x, northwest_y, r//2, depth - 1)

        # recursively draw another pattern in the top right (northeast)
        northeast_x = x + r
        northeast_y = y - r
        bubbles(northeast_x, northeast_y, r//2, depth - 1)

        # recursively draw another pattern in the bottom left (southwest)
        southwest_x = x - r
        southwest_y = y + r
        bubbles(southwest_x, southwest_y, r//2, depth - 1)

        # recursively draw another pattern in the bottom right (southeast)
        southeast_x = x + r
        southeast_y = y + r
        bubbles(southeast_x, southeast_y, r//2, depth - 1)


# the main function of the program
def main():
    # set the dimension of the canvas
    dim = 400
    
    # create the canvas
    picture.new_picture(dim, dim)

    # draw a background
    picture.set_fill_color("steelblue")
    picture.set_outline_color("steelblue")
    picture.draw_filled_square(0, 0, dim)

    # set bubble colors
    picture.set_fill_color("skyblue")
    picture.set_outline_color("skyblue")

    # find the center of the image
    center_x = dim // 2
    center_y = dim // 2

    # make the diameter of the big circle half of the canvas
    r = dim // 4   #radius is half the diameter

    # draw the bubbles, up to a depth of 4
    depth = 4
    bubbles(center_x, center_y, r, depth)

    # display the finished fractal
    picture.save_picture("bubbles.png")


# run the program
if __name__ == "__main__":
    main()
