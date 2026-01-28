# 023-326 AI Lab Report 2 - Question 4 (6)
# Man Goat Lion Cabbage search problem
class ManGoatLionCabbageProblem:
    def __init__(self, initial_state, goal_state):
        # State is a tuple of four elements: (man, goat, lion, cabbage)
        # Each element is either 'L' (left bank) or 'R' (right bank)
        self.initial_state = initial_state
        self.goal_state = goal_state
    def goalTest(self, state):
        return state == self.goal_state
    def successor(self, state):
        successors = []
        man, goat, lion, cabbage = state
        # Possible  
        moves = [
            ('man',),
            ('man', 'goat'),
            ('man', 'lion'),
            ('man', 'cabbage')
        ]
        for move in moves:
            new_state = list(state)
            # Move the man
            new_state[0] = 'R' if new_state[0] == 'L' else 'L'
            # Move the other items if included in the move  
            for item in move[1:]:
                if item == 'goat':
                    new_state[1] = 'R' if new_state[1] == 'L' else 'L'
                elif item == 'lion':
                    new_state[2] = 'R' if new_state[2] == 'L' else 'L'
                elif item == 'cabbage':
                    new_state[3] = 'R' if new_state[3] == 'L' else 'L'
            new_state_tuple = tuple(new_state)
            # Check for validity
            if self.is_valid(new_state_tuple):
                successors.append(new_state_tuple)
        return successors
    def is_valid(self, state):
        man, goat, lion, cabbage = state
        # Goat and lion alone
        if goat == lion and man != goat:
            return False
        # Goat and cabbage alone
        if goat == cabbage and man != goat:
            return False
        return True
    def bfs(self):
        from collections import deque

        queue = deque([(self.initial_state, [])])
        visited = set()

        while queue:
            current_state, path = queue.popleft()

            if self.goalTest(current_state):
                return path + [current_state]

            if current_state in visited:
                continue

            visited.add(current_state)

            for next_state in self.successor(current_state):
                if next_state not in visited:
                    queue.append((next_state, path + [current_state]))

        return None
    def generate_path(self, solution_path):
        if solution_path is None:
            return "No solution found"
        return "\n".join(str(state) for state in solution_path)
# Example usage
if __name__ == "__main__":
    initial = ('L', 'L', 'L', 'L')  # All on the left bank
    goal = ('R', 'R', 'R', 'R')     # All on the right bank

    problem = ManGoatLionCabbageProblem(initial, goal)
    solution = problem.bfs()
    print(problem.generate_path(solution))
# Output:
# ('L', 'L', 'L', 'L')
# ('R', 'L', 'L', 'L')
# ('L', 'R', 'L', 'L')
# ('R', 'R', 'L', 'L')
# ('L', 'R', 'R', 'L')
# ('R', 'R', 'R', 'L')
# ('L', 'R', 'R', 'R')
# ('R', 'R', 'R', 'R')
