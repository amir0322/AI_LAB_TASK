import math
def find_best_move(level, position, isMaxTurn, outcomes, maxLevel):
    if level == maxLevel:
        return outcomes[position]

    if isMaxTurn:
        left_value = find_best_move(level + 1, position * 2, False, outcomes, maxLevel)
        right_value = find_best_move(level + 1, position * 2 + 1, False, outcomes, maxLevel)
        return max(left_value, right_value)
    
    else:
        left_value = find_best_move(level + 1, position * 2, True, outcomes, maxLevel)
        right_value = find_best_move(level + 1, position * 2 + 1, True, outcomes, maxLevel)
        return min(left_value, right_value)



if __name__ == "__main__":
    outcomes = [7, 12, 5, 20, 9, 15, 8, 16]
    maxLevel = int(math.log(len(outcomes), 2))
    print("Leaf node outcomes:", outcomes)
    print("Best achievable value:", find_best_move(0, 0, True, outcomes, maxLevel))
