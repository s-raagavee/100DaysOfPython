# HURDLE 1: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# TASK: Hurdles race 1
# Reeborg has entered a hurdles race. Make him run the course, following the path shown.
# What you need to know - The functions move() and turn_left().
# More advanced - You may have noticed that your solution has some repeated patterns. If you know how to define functions, define a function named jump() and use it to simplify your program.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    move()
    jump_hurdle()