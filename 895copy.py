
game = [[0,0],[0,0],[0,0]]

def is_balanced(game):
    gold = game[0][0] + game[1][0] + game[2][0]
    silver = game[0][1] + game[1][1] + game[2][1]
    
    return gold == silver

def game_over(game):
    return (game[0][0] == 0 and game[0][1] == 0) or (game[1][0] == 0 and game[1][1] == 0) or (game[2][0] == 0 and game[2][1] == 0)

def game_generator(m):
    """
    Generate all possible game configurations
    
    :param m: Maximum total height for each stack
    :return: List of all valid game configurations
    """
    valid_games = []
    
    # Iterate through all possible configurations
    for i0 in range(m + 1):
        for j0 in range(m + 1 - i0):
            for i1 in range(m + 1):
                for j1 in range(m + 1 - i1):
                    for i2 in range(m + 1):
                        for j2 in range(m + 1 - i2):
                            # Current game configuration
                            game = [
                                [i0, j0],
                                [i1, j1],
                                [i2, j2]
                            ]
                            
                            # Check if balanced
                            if is_balanced(game):
                                if not game_over(game):
                                    valid_games.append(game)
    
    return valid_games

for char in game_generator(3):
    print(char)

# from itertools import permutations

# def generate_stack_permutations(input_list, m):
#     if input_list[0] + input_list[1] > m:
#         return []
#     g_count, s_count = input_list
#     items = ['g'] * g_count + ['s'] * s_count
#     # Generate all unique permutations of the items
#     unique_permutations = set(permutations(items))
    
#     # Convert each permutation to a stack and limit its size to m
#     stacks = [list(p[:m]) for p in unique_permutations]
#     return stacks

# # Example usage:
# input_list = [3, 1]
# m = 4
# result = generate_stack_permutations(input_list, m)
# print(result)