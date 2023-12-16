from adafruit_servokit import ServoKit

# Initialize the ServoKit instance
kit = ServoKit(channels=16)

# Constants for minimum and maximum servo angles
MIN_ANGLE = 0
MAX_ANGLE = 90

# Function to reset all servos to the minimum angle
def reset_all_servos_to_min():
    for channel in range(16):
        kit.servo[channel].angle = MIN_ANGLE
    print(f"All servos reset to {MIN_ANGLE} degrees.")

# Function to reset all servos to the maximum angle
def reset_all_servos_to_max():
    for channel in range(16):
        kit.servo[channel].angle = MAX_ANGLE
    print(f"All servos reset to {MAX_ANGLE} degrees.")

# Main execution
if __name__ == "__main__":
    while True:
        user_input = input("Enter 'min' to reset to minimum, 'max' to reset to maximum, or 'exit' to quit: ")
        if user_input == 'min':
            reset_all_servos_to_min()
        elif user_input == 'max':
            reset_all_servos_to_max()
        elif user_input == 'exit':
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please enter 'min', 'max', or 'exit'.")

