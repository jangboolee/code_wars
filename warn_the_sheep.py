def warn_the_sheep(queue):

    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    else:
        for i, animal in enumerate(queue):
            if animal == "wolf":
                sheep_position = len(queue) - i - 1
                return f"Oi! Sheep number {sheep_position}! " \
                       f"You are about to be eaten by a wolf!"


if __name__ == '__main__':

    a = ["sheep", "sheep", "sheep", "wolf", "sheep"]
    b = ["sheep", "sheep", "wolf"]
    c = ["sheep", "wolf", "sheep", "sheep", "sheep"]

    print(warn_the_sheep(a)) # "Oi! Sheep number 1! You are about to be eaten by a wolf!"
    print(warn_the_sheep(b)) # "Pls go away and stop eating my sheep"
    print(warn_the_sheep(c)) # "Oi! Sheep number 3! You are about to be eaten by a wolf!"