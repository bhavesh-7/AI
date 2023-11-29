def is_valid(state):
    m1, c1, b1, m2, c2 = state
    return (m1 >= 0 and c1 >= 0 and m2 >= 0 and c2 >= 0 and
            (m1 == 0 or m1 >= c1) and (m2 == 0 or m2 >= c2))

def goal_state(state):
    return state == (0, 0, 0, 3, 3)

def get_next_states(state):
    m1, c1, b1, m2, c2 = state
    next_states = []

    if b1 == 1:
        # Boat is on the left side
        for i in range(1, 3 + 1):
            for j in range(1, 3 + 1):
                if 0 < i + j <= 2:
                    next_state = (m1 - i, c1 - j, 0, m2 + i, c2 + j)
                    if is_valid(next_state):
                        next_states.append(next_state)
    else:
        # Boat is on the right side
        for i in range(1, 3 + 1):
            for j in range(1, 3 + 1):
                if 0 < i + j <= 2:
                    next_state = (m1 + i, c1 + j, 1, m2 - i, c2 - j)
                    if is_valid(next_state):
                        next_states.append(next_state)

    return next_states

def dfs(current_state, path):
    if goal_state(current_state):
        return path
    for next_state in get_next_states(current_state):
        if next_state not in path:
            new_path = dfs(next_state, path + [next_state])
            if new_path is not None:
                return new_path
    return None

def print_solution(solution):
    for i, state in enumerate(solution):
        print(f"Step {i + 1}: {state[:3]} | {state[3:]}")

initial_state = (3, 3, 1, 0, 0)
solution = dfs(initial_state, [initial_state])

if solution is not None:
    print("Solution found!\n")
    print_solution(solution)
else:
    print("No solution found.")
