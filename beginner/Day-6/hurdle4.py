# HURDLE 4: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Task: Hurdles race 4
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position, the height and the number of hurdles changes each time this world is reloaded.
# What you need to know
# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.
# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    
    if is_facing_north() and right_is_clear():
        turn_right()
        move()
        
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()
    
    elif wall_in_front():
        turn_left()
    
    elif wall_on_right():
        move()
    