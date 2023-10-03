#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say " Only the smart kid gets candy! Press the answer of this puzzle in the keyboard."

mapfile -t lines < 'puzzles.txt'

num_puzzles=$((${#lines[@]} / 2))

random_puzzle=$((RANDOM % num_puzzles))

puzzle_index=$((random_puzzle * 2))
puzzle="${lines[puzzle_index]}"
answer_index=$((puzzle_index + 1))
answer="${lines[answer_index]}"

say "$puzzle"

read -p "Enter your answer: " user_answer

expected_answer="${answer##*: }"

if [ "$user_answer" -eq "$expected_answer" ]; then
    say "Congratulations! You answered correctly. Here is your candy"
else
    say "Sorry, your answer is incorrect. The correct answer is $expected_answer."
fi

python puzzle_prompting.py