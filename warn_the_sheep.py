def warn_the_sheep(queue: list) -> str:

    # If wolf is the closest animal
    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    # If the wolf is somewhere in the queue
    else:
        # Loop through the queue while tracking the index
        for i, animal in enumerate(queue):
            # Stop when the wolf is found
            if animal == "wolf":
                # Calculate position of the sheep in danger
                sheep_position = len(queue) - i - 1
                # Return warning message
                return f"Oi! Sheep number {sheep_position}! " \
                       f"You are about to be eaten by a wolf!"


if __name__ == '__main__':

    a = ["sheep", "sheep", "sheep", "wolf", "sheep"]
    b = ["sheep", "sheep", "wolf"]
    c = ["sheep", "wolf", "sheep", "sheep", "sheep"]

    print(warn_the_sheep(a)) # "Oi! Sheep number 1! You are about to be eaten by a wolf!"
    print(warn_the_sheep(b)) # "Pls go away and stop eating my sheep"
    print(warn_the_sheep(c)) # "Oi! Sheep number 3! You are about to be eaten by a wolf!"