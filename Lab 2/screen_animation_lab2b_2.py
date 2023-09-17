while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    # Draw several diamonds with random colors and positions
    for _ in range(10):
        # Generate random coordinates for the diamond
        x = randint(0, width - 20)
        y = randint(0, height - 20)
        
        # Generate a random color
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        
        # Draw a diamond shape
        draw.polygon([
            (x+10, y),
            (x, y+10),
            (x+10, y+20),
            (x+20, y+10)
        ], fill=color, outline="white")

    # Display image
    disp.image(image, rotation)
    time.sleep(0.1) # Adjust the sleep time to control the speed of the animation
