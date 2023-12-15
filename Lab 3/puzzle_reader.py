import qwiic_keypad
import time
import sys
import subprocess
import random

def say(text):
    subprocess.call(['/usr/bin/mplayer', '-ao', 'alsa', '-really-quiet', '-noconsolecontrols', 
                     f'http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={text}&tl=en'])

def get_puzzle_and_answer():
    with open('puzzles.txt', 'r') as file:
        lines = file.readlines()
    
    num_puzzles = len(lines) // 2
    random_puzzle = random.randint(0, num_puzzles - 1)

    puzzle_index = random_puzzle * 2
    puzzle = lines[puzzle_index].strip()
    
    answer_index = puzzle_index + 1
    answer = lines[answer_index].strip().split(":")[1].strip()  # Extracting the answer after the colon
    
    return puzzle, answer

def runExample():

    print("\nSparkFun qwiic Keypad Example\n")
    myKeypad = qwiic_keypad.QwiicKeypad(0x4b)

    if myKeypad.is_connected() == False:
        print("The Qwiic Keypad device isn't connected to the system. Please check your connection", 
              file=sys.stderr)
        return

    myKeypad.begin()

    button = 0
    user_answer = ""

    puzzle, expected_answer = get_puzzle_and_answer()
    say(" Only the smart kid gets candy! Press the answer of this puzzle on the keyboard.")
    time.sleep(0.5)
    say(puzzle)
    say("Enter your answer and press pound key:")

    while True:
        # necessary for keypad to pull button from stack to readable register
        myKeypad.update_fifo()
        button = myKeypad.get_button()

        if button == -1:
            print("No keypad detected")
            time.sleep(1)
        elif button != 0:
            # Get the character version of this char
            charButton = chr(button)
            if charButton == '#':  # Assuming '#' denotes end of input
                print(user_answer)
                if user_answer == expected_answer:
                    say("Congratulations! You answered correctly. Here is your candy.")
                    subprocess.call(['python', 'main.py'])
                else:
                    say(f"Sorry, your answer ({user_answer}) is incorrect. The correct answer is {expected_answer}.")
                    subprocess.call(['python', 'main.py'])
            elif charButton == '*':
                user_answer = ""  # Assuming '*' clears the input
                print(" ", end="")
            else:
                print(charButton, end="")
                user_answer += charButton

            # Flush the stdout buffer to give immediate user feedback
            sys.stdout.flush()

        time.sleep(0.25)

if __name__ == "__main__":
    runExample()
