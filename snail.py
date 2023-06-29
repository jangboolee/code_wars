def snail(snail_map: list) -> list:

    # Get the dimension of the array
    n = len(snail_map)

    snail_path = []
    # Add the top outermost elements
    snail_path.extend(snail_map[0])
    # Add the right outermost elements
    for i in range(1, n):
        snail_path.append(snail_map[i][n-1])
    # Add the bottom outermost elements in reverse
    snail_path.extend(snail_map[n-1][:n-1][::-1])
    

    pass


if __name__ == '__main__':

    array_0 = ['a b c d'.split(' '),
               'e f g h'.split(' '),
               'i j k l'.split(' '),
               'm n o p'.split(' ')]
    print(snail(array_0))

    array_1 = [[1,2,3],
               [4,5,6],
               [7,8,9]]
    print(snail(array_1))  # [1,2,3,6,9,8,7,4,5]

    array_2 = [[1,2,3],
               [8,9,4],
               [7,6,5]]
    print(snail(array_2))  # [1,2,3,4,5,6,7,8,9]