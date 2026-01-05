"""
Example: Computing upper bound using knapsack scheduling relaxation

This simplified code excerpt shows the key logic for bound computation
in the branch-and-bound algorithm.
"""

def compute_upper_bound(node, items, remaining_budget, m):
    """
    Compute upper bound for a partial solution.
    
    Args:
        node: Current search node with partial selection
        items: List of remaining items (duration, price)
        remaining_budget: Budget left after current selection
        m: Number of machines
    
    Returns:
        Upper bound on best makespan achievable from this node
    """
    # Part 1: Contribution from already-decided items
    committed_value = 0
    for i in range(node.depth):
        quantity = node.occurrences[i]
        duration = items[i].duration
        # Ceiling: minimum time slots needed for quantity jobs
        committed_value += duration * math.ceil(quantity / m)
    
    # Part 2: Solve ceiling knapsack for remaining items
    # This is the relaxed upper bound
    relaxed_value = solve_ceiling_knapsack(
        items=items[node.depth+1:],  # Undecided items
        budget=remaining_budget,
        m=m
    )
    
    # Total upper bound
    upper_bound = committed_value + relaxed_value
    
    return upper_bound


def solve_ceiling_knapsack(items, budget, m):
    """
    Solve ceiling knapsack problem using dynamic programming.
    
    Maximize sum(duration[i] * ceil(quantity[i] / m))
    Subject to: sum(price[i] * quantity[i]) <= budget
    """
    n = len(items)
    dp = {}  # State: (item_index, remaining_budget) -> max_value
    
    def recurse(i, b):
        if i == n or b == 0:
            return 0
        
        if (i, b) in dp:
            return dp[(i, b)]
        
        # Try different quantities of item i
        best = 0
        max_qty = b // items[i].price
        
        for qty in range(max_qty + 1):
            cost = qty * items[i].price
            value = items[i].duration * math.ceil(qty / m)
            future = recurse(i + 1, b - cost)
            best = max(best, value + future)
        
        dp[(i, b)] = best
        return best
    
    return recurse(0, budget)
