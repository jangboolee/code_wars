def dirReduc(arr: list) -> list:

    # Create mapping table of opposite directions
    dir_opposites: dict = {
        "NORTH": "SOUTH",
        "WEST": "EAST",
        "SOUTH": "NORTH",
        "EAST": "WEST"
    }

    i: int
    final_dir: list = []
    for i in range(len(arr)):
        # If final_dir is empty
        if len(final_dir) == 0:
            # Add the current direction
            final_dir.append(arr[i])
        # If the latest direction in final_dir is the opposite direction of
        # the current direction
        elif final_dir[-1] == dir_opposites[arr[i]]:
            # Remove the latest added direction in final_dir
            final_dir.pop()
        # If the latest direction is not the opposite direction
        else:
            # Add the current direction to final_dir
            final_dir.append(arr[i])

    return final_dir


if __name__ == '__main__':

    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    print(dirReduc(a))    # ['WEST']
    
    u = ["NORTH", "WEST", "SOUTH", "EAST"]
    print(dirReduc(u))    # ["NORTH", "WEST", "SOUTH", "EAST"]
