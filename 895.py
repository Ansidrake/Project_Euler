def is_valid_move(stack, is_gold_turn):
    """
    Check if a valid move exists for the current player.
    
    :param stack: A list representing a stack of coins
    :param is_gold_turn: Boolean indicating if it's gold player's turn
    :return: Boolean indicating if a valid move exists
    """
    if not stack:
        return False
    
    for i, coin in enumerate(stack):
        if coin == 'G' and is_gold_turn:
            return True
        if coin == 'S' and not is_gold_turn:
            return True
    
    return False

def make_move(stack, is_gold_turn):
    """
    Simulate removing a coin and all coins above it.
    
    :param stack: A list representing a stack of coins
    :param is_gold_turn: Boolean indicating if it's gold player's turn
    :return: New stack after the move
    """
    for i, coin in enumerate(stack):
        if coin == 'G' and is_gold_turn:
            return stack[i+1:]
        if coin == 'S' and not is_gold_turn:
            return stack[i+1:]
    
    return stack  # This should never happen if is_valid_move is called first

def is_fair_arrangement(stacks):
    """
    Determine if the arrangement is fair by simulating all possible first moves.
    
    :param stacks: List of stacks, where each stack is a list of coins ('G' or 'S')
    :return: Boolean indicating if the arrangement is fair
    """
    def play_game(current_stacks, is_gold_turn):
        """
        Recursive game simulation to determine if first player loses.
        
        :param current_stacks: Current game state
        :param is_gold_turn: Whose turn it is
        :return: Boolean indicating if current player will lose
        """
        # Check if any stack has a valid move
        valid_moves_exist = any(
            is_valid_move(stack, is_gold_turn) for stack in current_stacks
        )
        
        if not valid_moves_exist:
            # Current player cannot move, so they lose
            return True
        
        # Try all possible moves
        for i in range(len(current_stacks)):
            if is_valid_move(current_stacks[i], is_gold_turn):
                # Make a copy of stacks and make a move
                new_stacks = current_stacks.copy()
                new_stacks[i] = make_move(new_stacks[i], is_gold_turn)
                
                # If the opponent loses after this move, current player wins
                if not play_game(new_stacks, not is_gold_turn):
                    return False
        
        # If no move guarantees a win, current player loses
        return True

    # Test both Gary (gold) and Sally (silver) starting
    return play_game(stacks, True) and play_game(stacks, False)

def generate_arrangements(max_height):
    """
    Generate all possible fair and balanced arrangements.
    
    :param max_height: Maximum height of each stack
    :return: Number of fair and balanced arrangements
    """
    fair_arrangements = 0
    
    # Generate all possible coin combinations
    from itertools import product
    
    # Ensure total gold and silver coins are equal
    for stack1 in product(['G', 'S'], repeat=1):
        for stack2 in product(['G', 'S'], repeat=2):
            for stack3 in product(['G', 'S'], repeat=3):
                # Flatten and count coins
                all_coins = list(stack1) + list(stack2) + list(stack3)
                if all_coins.count('G') == all_coins.count('S'):
                    # Check if arrangement is fair
                    if is_fair_arrangement([list(stack1), list(stack2), list(stack3)]):
                        fair_arrangements += 1
    
    return fair_arrangements

# Verify known values
print("G(2):", generate_arrangements(2))  # Should output 6
print("G(5):", generate_arrangements(5))  # Should output 348