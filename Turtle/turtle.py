import turtle

# Set up the turtle
t = turtle.Turtle()

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

# Main function to execute the drawing
def main():
    t.speed(1)  # Set the speed of the turtle
    draw_triangle()  # Call the draw_triangle function
    turtle.done()  # Keep the window open

# Call the main function to start drawing
main()
