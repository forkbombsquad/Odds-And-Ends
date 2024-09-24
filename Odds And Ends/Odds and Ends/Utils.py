from random import randint

def rand(min_val: int, max_val: int) -> int:
    if max_val == min_val:
        return max_val
    return randint(min_val, max_val)

def generateStandardDieSides(max_val: int) -> [int]:
    sides = []
    count = 0
    while count < max_val:
        sides.append(count + 1)
        count += 1
    return sides