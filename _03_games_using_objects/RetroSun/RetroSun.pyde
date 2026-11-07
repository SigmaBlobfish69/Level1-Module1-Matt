global bg_color, sun_colors, sun_radius, sections
sections = []

sun_radius = 250
bg_color = color(31, 0, 48)

# RGB colors
sun_colors = [
  color(212, 202, 11), 
  color(214, 198, 30), 
  color(211, 170, 26), 
  color(216, 157, 51), 
  color(217, 124, 64), 
  color(213, 104, 81), 
  color(212, 51, 98), 
  color(215, 29, 121), 
  color(217, 11, 139), 
  color(217, 0, 151)
]

"""
*
* LOOK AT RetroSun.html IN THIS FOLDER to see what you will be creating!
*
"""

def setup():
    global sections
    pass
    # TODO 1) Set the size of your sketch
    size(600, 400)
    """
    * PART I: Drawing the sun
    * See 1st image 
    """

    # TODO 2) Draw the bg_color background color using the background() function
    background(bg_color)
    # TODO 3) Draw an ellipse for the sun in the center of the window
    # Use fill(sun_colors[0]) to make it yellow
    # Use noStroke() to remove the black outline
    noStroke()
    fill(sun_colors[0])
    ellipse(width/2, height/2, sun_radius * 2, sun_radius * 2)
    # Do you see a yellow sun like in the 1st image?
    # If not, fix your code before proceeding.
    
    """
    * PART II: Drawing a color gradient on the sun
    * See 2nd image
    *
    * This will make the sun have gradually different colors from the 
    * top to bottom
    """
    
    # Call the loadPixels() function to load the pixels list variable.
    loadPixels()
    # Loop through all the pixels in your window.
    # A pixel is a 1x1 square, so if your window width is 600 and the 
    # height is 400 (600x400), then there are 600 * 400 = 240,000 pixels
    for i in range(len(pixels)):
        if pixels[i] == sun_colors[0]:
            y = i // width
            sun_top_y = height/2 - sun_radius
            sun_bottom_y = height/2 + sun_radius
            step = map(y, sun_top_y, sun_bottom_y, 0, 1)
            c = interpolate_color(sun_colors, step)
            pixels[i] = c

    # Call updatePixels() to apply the changes made to the pixels list
    updatePixels()
    
    for i in range(5):
        x = width/2 - sun_radius
        y = 250 + (i * 35)
        w = sun_radius * 2
        h = 20

        sections.append(Rectangle(x, y, w, h))

def draw():

    # Redraw the background
    background(bg_color)

    # Redraw the sun
    noStroke()
    fill(sun_colors[0])
    ellipse(width/2, height/2, sun_radius*2, sun_radius*2)

    # Redraw the gradient
    loadPixels()

    for i in range(len(pixels)):
        if pixels[i] == sun_colors[0]:
            y = i // width
            sun_top_y = height/2 - sun_radius
            sun_bottom_y = height/2 + sun_radius
            step = map(y, sun_top_y, sun_bottom_y, 0, 1)
            c = interpolate_color(sun_colors, step)
            pixels[i] = c

    updatePixels()

    # Move and draw the missing sun sections
    for section in sections:
        section.update()
        section.draw()

    """
    * PART IV: Moving the missing sun sections
    *
    * To move a section upwards each rectangle's y value needs to decrease.
    * To make the section get smaller, its height needs to also decrease.
    """
   
    # Decrease the y variable of the rectangular section created in part III.
    # If there isn't a variable declare a variable OUTSIDE of the draw
    # function AND initialize it in the setup() function.
    # *HINT* You will have to put 'global y', where y is your variable,
    #        in setup() and draw()
   
    # Do you see the rectangle moving upwards?
    # See image 4
   
    # Pick a y positon to be the location when the sections stop moving up.
    # If the rectangle's y positon is above this, move the rectangle's
    # y position back to the bottom of the sun.

    # Does the rectangle move back to the bottom?
   
    # Decrease the the height of the rectangle as it moves upwards.
    # Similar to the y positon, a variable for the height needs to be
    # created if it doesn't already exist.

    # Adjust the amount to decrease so that it disappears close to the top.
    
    # Add code to reset the height of the rectangle when it moves back to
    # the bottom of the sun.
    # See image 5
   
    """
    * PART V: Moving more missing sun sections
    *
    * Using a loop to manage moving multiple missing sun sections 
    """
   
    # Figure out how to create the other missing sun sections using the
    # code you wrote for the 1 missing sun section.
    # *HINT* You can use the Rectangle class defined below to create
    #        a list of rectangles and a loop to iterate through each one.


    """
    * PART VI: Adding extras
    *
    * If you want to make your retro sun look more unique, try adding
    * reflections and stars.
    """    
    fill(255)
    noStroke()

    ellipse(80, 60, 5, 5)
    ellipse(500, 80, 5, 5)
    ellipse(450, 300, 5, 5)
    ellipse(100, 320, 5, 5)
    ellipse(530, 180, 5, 5)

# Variable step should be between 0 and 1, inclusive
def interpolate_color(color_list, step):
    sz = len(color_list)
  
    if sz == 1 or step <= 0.0:
        return color_list[0]
    elif step >= 1.0:
        return color_list[sz - 1]
  
    scl = step * (sz - 1)
    i = int(scl)
  
    return lerpColor(color_list[i], color_list[i + 1], scl - i)

# Feel free to use this class to create a list of missing
# sections in the sun, for example:
# sections = list()
# for i in range(5):
#     sections.append(Rectangle(x, y, w, h)) # Create your own x, y, w, h variables
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def draw(self):
        noStroke()
        fill(bg_color)
        rect(self.x, self.y, self.w, self.h)

    def update(self):
        self.y -= 1
        self.h -= 40.0 / (sun_radius + (sun_radius/4))
        
        if self.y < (height / 2) - (sun_radius / 4):
            self.y = (height / 2) + sun_radius
            self.h = 40
