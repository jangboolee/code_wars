def is_valid_walk(walk):
    # If it doesn't take exactly 10 minutes
    if len(walk) != 10:
        return False
    # If it takes exactly 10 minutes and you return to the original point
    elif (walk.count('n') == walk.count('s')) and (walk.count('w') == walk.count('e')):
        return True
    # For all other cases
    else:
        return False
