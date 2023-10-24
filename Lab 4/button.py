import time
import qwiic_button

button = qwiic_button.QwiicButton()

while True:
    # Check if the button is pressed and tell us if it is!
    if button.is_button_pressed():
        print("The button is pressed!")
        while button.is_button_pressed():
            time.sleep(1)  # Wait for the user to stop pressing
    time.sleep(0.02)  # Don't hammer too hard on the I2C bus
