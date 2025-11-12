def calculate_floor(moves):
    floor = 0
    for move in moves:
        if move == "U":
            floor += 1
        elif move == "D":
            floor -= 1
    return floor
