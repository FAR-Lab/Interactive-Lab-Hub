from adafruit_servokit import ServoKit
import time

# Create the ServoKit instance
kit = ServoKit(channels=16)
# Example: Move servos in a wave pattern



from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)


def move_servo(channel, angle, delay=0.01):
    kit.servo[channel].angle = angle
    time.sleep(delay)
    print(f"Servo {channel} moved to {angle} degrees.")

# Function to move a group of 4 servos to a specified angle
def move_servo_group(start_channel, end_channel, angle):
    for channel in range(start_channel, end_channel):
        kit.servo[channel].angle = angle
    
        # kit.servo[channel].angle = 60
    print(f"Servos {start_channel} to {end_channel - 1} moved to {angle} degrees.")


def move_servos_top_down(angle):
    for start_channel in range(0, 16, 4):
        move_servo_group(start_channel, start_channel + 4, angle)
        
        # Check if we need to reset the previous group
        if start_channel >= 4:
            prev_group_start = start_channel - 4
            move_servo_group(prev_group_start, prev_group_start + 4, 60)
    
        time.sleep(0.1)
    move_servo_group(12, 16, 60)

# Move servos bottom-up
def move_servos_bottom_up(angle):
    for start_channel in range(12, -1, -4):
        move_servo_group(start_channel, start_channel + 4, angle)
        time.sleep(0.1)

# Move servos left-to-right
def move_servos_left_right(angle):
    for column_start in range(4):
        for row in range(4):
            servo_channel = column_start + row * 4
            move_servo(servo_channel, angle)
        time.sleep(0.1)


# Move servos right-to-left
def move_servos_right_left(angle):
    for column_start in range(3, -1, -1):  # Iterate over columns in reverse order
        for row in range(4):  # Iterate over rows
            servo_channel = column_start + row * 4  # Calculate the servo channel
            move_servo(servo_channel, angle)
        time.sleep(0.1)


def move_servos_center_out(angle):
    center_servos = [5, 6, 9, 10]
    outer_servos = [i for i in range(16) if i not in center_servos]

    for servo in center_servos:
        move_servo(servo, angle)
    time.sleep(0.1)

    for servo in outer_servos:
        move_servo(servo, angle)
    time.sleep(0.1)

# Move servos outer 12 to center 4
def move_servos_out_center(angle):
    center_servos = [5, 6, 9, 10]
    outer_servos = [i for i in range(16) if i not in center_servos]

    for servo in outer_servos:
        move_servo(servo, angle)
    time.sleep(0.1)

    for servo in center_servos:
        move_servo(servo, angle)
    time.sleep(0.1)

def move_servos_in_order(target_angle, speed_delay=0.1):
    # Define the order of servo movement
    servo_order = [0, 4, 8, 12, 13, 14, 15, 11, 7, 3, 2, 1, 5, 9, 6, 10]

    # Move each servo in the defined order
    for servo in servo_order:
        kit.servo[servo].angle = target_angle
        time.sleep(speed_delay) 

def move_servos_in_reverse_order(target_angle, speed_delay=0.1):
    # Define the order of servo movement
    servo_order = [0, 4, 8, 12, 13, 14, 15, 11, 7, 3, 2, 1, 5, 9, 6, 10]
    reversed_servo_order = servo_order[::-1]

    # Move each servo in the defined order
    for servo in reversed_servo_order:
        kit.servo[servo].angle = target_angle
        time.sleep(speed_delay) 

# Move servos in a left down diagonal pattern
def move_servos_left_down(angle):
    sequences = [[0], [1, 4], [2, 5, 8], [3, 6, 9, 12], [7, 10, 13], [11, 14], [15]]
    for group in sequences:
        for servo in group:
            move_servo(servo, angle)
        time.sleep(0.1)

# Move servos in a right down diagonal pattern
def move_servos_right_down(angle):
    sequences = [[3], [2, 7], [1, 6, 11], [0, 5, 10, 15], [4, 9, 14], [8, 13], [12]]
    for group in sequences:
        for servo in group:
            move_servo(servo, angle)
        time.sleep(0.1)

# Move servos in a left up diagonal pattern
def move_servos_left_up(angle):
    sequences = [[12], [8, 13], [4, 9, 14], [0, 5, 10, 15], [1, 6, 11], [2, 7], [3]]
    for group in sequences:
        for servo in group:
            move_servo(servo, angle)
        time.sleep(0.1)

# Move servos in a right up diagonal pattern
def move_servos_right_up(angle):
    sequences = [[15], [11, 14], [7, 10, 13], [3, 6, 9, 12], [2, 5, 8], [1, 4], [0]]
    for group in sequences:
        for servo in group:
            move_servo(servo, angle)
        time.sleep(0.1)

def move_servos_idd(angle, angle1):
    sequences = [[0, 4, 8, 12, 5, 6, 9, 10, 3, 7, 11, 15], [1, 2, 4, 8, 7, 11, 0, 13, 14, 3], [1, 2, 4, 8, 7, 11, 0, 13, 14, 3]]
    for group in sequences:
        # Move all servos in the group to the first angle
        for servo in group:
            move_servo(servo, angle)
        
        # Optional: Wait for some time after moving all servos in the group to the first angle
        time.sleep(0.6)  # Adjust the delay as needed

        # Move all servos in the group to the second angle
        for servo in group:
            move_servo(servo, angle1)
        
        # Wait for some time before proceeding to the next group
        time.sleep(0.6)  # Adjust the delay as needed

def move_servos_idd(angle, angle1):
    sequences = [[0, 4, 8, 12, 5, 6, 9, 10, 3, 7, 11, 15], [1, 2, 4, 8, 7, 11, 0, 13, 14, 3], [1, 2, 4, 8, 7, 11, 0, 13, 14, 3]]
    for group in sequences:
        # Move all servos in the group to the first angle
        for servo in group:
            move_servo(servo, angle)
        
        # Optional: Wait for some time after moving all servos in the group to the first angle
        time.sleep(0.6)  # Adjust the delay as needed

        # Move all servos in the group to the second angle
        for servo in group:
            move_servo(servo, angle1)
        
        # Wait for some time before proceeding to the next group
        time.sleep(0.6)  # Adjust the delay as needed

def move_servo_sequence(sequence, angle, angle1):
    for group in sequence:
        for servo in group:
            move_servo(servo, angle)
        time.sleep(0.6)
        for servo in group:
            move_servo(servo, angle1)
        time.sleep(0.6)

def move_servos_alphabet(angle, angle1):
    alphabet_sequences = {
    'A': [[1, 2, 3, 4, 6, 9, 10, 11]],
    'B': [[0, 1, 2, 3, 5, 7, 9, 10, 11]],
    'C': [[1, 2, 4, 7, 8, 11, 12, 15]],
    'D': [[1, 2, 4, 8, 7, 11, 0, 13, 14, 3]],
    'E': [[0, 1, 2, 3, 4, 8, 12, 7, 11, 15, 5]],
    'F': [[0, 1, 2, 3, 4, 8, 6, 10]],
    'G': [[1, 2, 4, 7, 8, 11, 12, 15, 10]],
    'H': [[0, 1, 2, 3, 5, 9, 14, 13, 12, 15]],
    'I': [[0, 4, 8, 12, 5, 6, 9, 10, 3, 7, 11, 15]],
    'J': [[2, 3, 7, 11, 8, 9, 10]],
    'K': [[0, 1, 2, 3, 6, 9, 12, 11]],
    'L': [[0, 1, 2, 3, 7, 11]],
    'M': [[2, 3, 4, 5, 10, 11, 12, 13]],
    'N': [[0, 1, 2, 3, 5, 10, 12, 13, 14, 15]],
    'O': [[1, 2, 4, 7, 8, 11, 13, 14]],
    'P': [[0, 1, 2, 3, 4, 6, 9]],
    'Q': [[1, 2, 4, 7, 8, 11, 13, 14, 15]],
    'R': [[0, 1, 2, 3, 4, 6, 9, 11]],
    'S': [[4, 8, 12, 5, 10, 3, 7]],
    'T': [[0, 4, 8, 12, 5, 6, 7]],
    'U': [[0, 1, 2, 12, 13, 14, 7, 11]],
    'V': [[1, 6, 11, 14]],
    'W': [[0, 1, 6, 7, 8, 9, 14, 15]],
    'X': [[0, 5, 10, 15, 12, 3]],
    'Y': [[1, 6, 7, 9, 12]],
    'Z': [[0, 4, 8, 12, 6, 9, 3, 7, 11, 15]]
}

    for letter, sequence in alphabet_sequences.items():
        print(f"Moving servos for letter: {letter}")
        move_servo_sequence(sequence, angle, angle1)

def servo_move_smile(target_angle):
    # Define the specific servos to move
    specific_servos = [0, 12, 2, 7, 11, 14]

    # Set the angle for each specific servo
    for servo in specific_servos:
        kit.servo[servo].angle = target_angle

    # Optionally, add a delay after setting the angles if needed
    time.sleep(0.3) 

def servo_move_cry(target_angle):
    # Define the specific servos to move
    specific_servos = [0, 12, 3, 6, 10, 15]

    # Set the angle for each specific servo
    for servo in specific_servos:
        kit.servo[servo].angle = target_angle

    # Optionally, add a delay after setting the angles if needed
    time.sleep(0.3) 

# Main function to execute the servo movements based on user input
def main():
    try:
        while True:
            user_input = input("Enter '1' for top-down, '2' for bottom-up, '3' for left-right, '4' for right-left, '5' for left-down, '6' for right-down, '7' for left-up, '8' for right-up, '9' for center-out, '10' for out-center, 'reset' to move them to 90 degrees, or 'exit' to quit: ")
            if user_input == '1':
                # move_servos_top_down_combined(60)
                move_servos_top_down(0)
            elif user_input == '2':
                move_servos_bottom_up(0)
                move_servos_bottom_up(60)
            elif user_input == '3':
                move_servos_left_right(0)
                move_servos_left_right(60)
            elif user_input == '4':
                move_servos_right_left(0)
                move_servos_right_left(60)
            elif user_input == '5':
                move_servos_left_down(0)
                move_servos_left_down(60)
            elif user_input == '6':
                move_servos_right_down(0)
                move_servos_right_down(60)
            elif user_input == '7':
                move_servos_left_up(0)
                move_servos_left_up(60)
            elif user_input == '8':
                move_servos_right_up(0)
                move_servos_right_up(60)
            elif user_input == '9':
                move_servos_center_out(0)
                move_servos_center_out(60)
            elif user_input == '10':
                move_servos_out_center(0)
                move_servos_out_center(60)
            elif user_input == '11':
                move_servos_idd(0,60)
            elif user_input == '12':
                move_servos_alphabet(0, 60)
            elif user_input == '13':
                move_servos_in_order(0)
                move_servos_in_order(60)
            elif user_input == '14':
                move_servos_in_reverse_order(0)
                move_servos_in_reverse_order(60)
            elif user_input == '15':
                servo_move_smile(0)
                servo_move_smile(60)
            elif user_input == '16':
                servo_move_cry(0)
                servo_move_cry(60)
            elif user_input == 'exit':
                print("Exiting program.")
                break
            else:
                print("Invalid input. Please enter a valid command.")
    except KeyboardInterrupt:
        print("\nProgram terminated.")

if __name__ == "__main__":
    main()
