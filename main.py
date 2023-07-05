import copy

# Making known the initial state
init_state = [[1, 2, 3], [], []]

# Defining the goal state
Goal_State = [[], [], [1, 2, 3]]

# Goal test function
def is_goal(state):
    s1 = state[0]
    s2 = state[1]
    s3 = state[2]
    if s1 == Goal_State[0] and s2 == Goal_State[1] and s3 == Goal_State[2]:
        return True
    return False

# Move objects from one stack to another
def move_objects(state, from_stack, to_stack):
    new_state = copy.deepcopy(state)
    from_stack_idx = from_stack - 1
    to_stack_idx = to_stack - 1
    if len(new_state[from_stack_idx]) == 0 or len(new_state[to_stack_idx]) == 3:
        return None
    item = new_state[from_stack_idx].pop(0)
    new_state[to_stack_idx].insert(0, item)
    return new_state

# Breadth-First Search (BFS) algorithm
def bfs(start_state):
    open_list = [start_state]
    closed_list = []
    expanded_nodes = 0

    while open_list:
        print("open:", open_list)
        print("closed:", closed_list)
        state = open_list.pop(0)
        expanded_nodes += 1

        if is_goal(state):
            print("Goal found! Expanded", expanded_nodes, "nodes.")
            print(closed_list)
            break

        closed_list.append(state)

        for i in range(1, 4):
            for j in range(1, 4):
                if i != j:
                    new_state = move_objects(state, i, j)
                    if new_state is not None and new_state not in closed_list and new_state not in open_list:
                        open_list.append(new_state)

# Driver code
bfs(init_state)
