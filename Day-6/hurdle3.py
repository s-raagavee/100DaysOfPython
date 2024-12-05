# HURDLE 3: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# Task:Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position and number of hurdles changes each time this world is reloaded.
# What you need to know
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    
    if wall_in_front() and wall_on_right():
        turn_left()
    
    elif wall_on_right():
        move()
    
    elif right_is_clear() and is_facing_north():
        turn_right()
        move()
        turn_right()
        move()