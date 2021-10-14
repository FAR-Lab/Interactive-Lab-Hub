import qwiic_i2c
import qwiic_button
import time
import sys

def run_example():

    print("\nSparkFun Qwiic Button Example 6")
    my_button = qwiic_button.QwiicButton(0x5b)

    if my_button.begin() == False:
        print("\nThe Qwiic Button isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
        
    print("\nButton ready!")

    print("\nEnter a new I2C address for the Qwiic Button to use.")
    print("\nDon't use the 0x prefix. For instance, if you wanted to")
    print("\nchange the address to 0x5B, you would type 5B and hit enter.")

    new_address = '5B'
    new_address = int(new_address, 16)

    # Check if the user entered a valid address
    if new_address > 0x08 and new_address < 0x77:
        print("\nCharacters received and new address valid!")
        print("\nAttempting to set Qwiic Button address...")

        my_button.set_I2C_address(new_address)
        print("\nAddress successfully changed!")
        # Check that the Qwiic Button acknowledges on the new address
        time.sleep(0.02)
        if my_button.begin() == False:
            print("\nThe Qwiic Button isn't connected to the system. Please check your connection", \
                file=sys.stderr)
            
        else:
            print("\nButton acknowledged on new address!")
            
    else:
        print("\nAddress entered not a valid I2C address")

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 6")
        sys.exit(0)
