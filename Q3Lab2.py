   # 3.	WAP in Python will implement DFS/BFS on the water jug problem.
   # Given a 4 - litre jug filled with water & an empty 3 - litre Jug, how can one obtain exactly 2 liters in 4 litres jug. There is no measuring mark on any of them.
   # •	Define WaterJug Class with a constructor to initialize the initial and goal state
   # •	Define boolean goalTest(current_state, goal_state) to check if current_state is goal_state or not
   # •	Define successor() with reference to the production rules to generate possible child(s).
   # •	Verify if successor() is working properly or not
    # •	Define DFS/BFS search algorithm to find the solution
    # •	Modify search algorithm to store state,parent in CLOSED list and also define generate_path() to provide the path of solution.
class WaterJug:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state  # (4, 0)
        self.goal_state = goal_state          # (2, x)

    def goalTest(self, current_state):
        return current_state[0] == self.goal_state[0]

    def successor(self, state):
        successors = []
        jug4, jug3 = state

        # Fill 4-litre jug
        if jug4 < 4:
            successors.append((4, jug3))

        # Fill 3-litre jug
        if jug3 < 3:
            successors.append((jug4, 3))

        # Empty 4-litre jug
        if jug4 > 0:
            successors.append((0, jug3))

        # Empty 3-litre jug
        if jug3 > 0:
            successors.append((jug4, 0))

        # Pour from 4-litre jug to 3-litre jug
        if jug4 > 0 and jug3 < 3:
            transfer = min(jug4, 3 - jug3)
            successors.append((jug4 - transfer, jug3 + transfer))

        # Pour from 3-litre jug to 4-litre jug
        if jug3 > 0 and jug4 < 4:
            transfer = min(jug3, 4 - jug4)
            successors.append((jug4 + transfer, jug3 - transfer))

        return successors
    def bfs(self):
        from collections import deque

        initial_state = self.initial_state
        goal_state = self.goal_state

        queue = deque([(initial_state, [])])
        visited = set()

        while queue:
            current_state, path = queue.popleft()

            if self.goalTest(current_state):
                return path + [current_state]

            if current_state in visited:
                continue

            visited.add(current_state)

            for successor in self.successor(current_state):
                if successor not in visited:
                    queue.append((successor, path + [current_state]))

        return None
    def generate_path(self, solution_path):
        if solution_path is None:
            return "No solution found"
        return " -> ".join(str(state) for state in solution_path)
# Example usage
water_jug = WaterJug((4, 0), (2, None))
solution_path = water_jug.bfs()
print(water_jug.generate_path(solution_path))

#output:
# (4, 0) -> (1, 3) -> (1, 0) -> (0, 1) -> (4, 1) -> (2, 3) -> (2, 0)
