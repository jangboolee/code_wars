def beeramid(bonus: int, price: int) -> int:

    # Number of beer cans that can be purchased with the bonus
    beer_cans = bonus // price

    # Build up beeramid from the top using the number of beer cans
    level = 0
    while (level + 1)**2 <= beer_cans:
        level += 1
        beer_cans -= level**2

    return level


print(beeramid(9, 2))
print(beeramid(21, 1.5))
print(beeramid(-1, 4))