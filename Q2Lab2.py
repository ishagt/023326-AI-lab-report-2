# Q2. Implement the Vacuum Cleaning agents efficiency by implementing a model-based agent. Provide your arguements
import random
class RoomCleanerAgent:
    def __init__(self, room_size=(10,10)):
        self.room_size = room_size;
        self.grid = [[random.choice([0,1]) for _ in range(room_size[1])]
             for _ in range(room_size[0])]
        self.current_position = (random.randint(0, room_size[0]-1), random.randint(0, room_size[1]-1))

    def display_room(self):
        for row in self.grid:
            print(" ".join(map(str,row)))
            print("\n")
    def perceive(self):
    # perceive current state
        x,y = self.current_position
        return self.grid[x][y]
    def act(self):
    # model-based agent action
        x,y = self.current_position
        if self.perceive() == 1: # if dirty
            print(f"cell ({x},{y}) is dirty. Cleaning...")
            self.grid[x][y] = 0 # clean the cell
            print(f"cell ({x},{y}) cleaned.")
        else:
            print(f"cell ({x},{y}) is clean. Moving...")
            self.move()
    def move(self):
    # move to a random adjacent cell
        x,y = self.current_position
        if y<self.room_size[1]-1:
            self.current_position = (x, y+1) # move right
        elif x<self.room_size[0]-1:
            self.current_position = (x+1, 0) # move down to next row    
        else:
            self.current_position = (0, 0) # reset to start
    def is_room_clean(self):
        return all(cell == 0 for row in self.grid for cell in row)
    def run(self):
        print("Initial room state:")
        self.display_room()
        steps = 0
        while not self.is_room_clean():
            if self.current_position is None:
                self.current_position = (0, 0)
            print(f"\nStep {steps+1}:")
            self.act()
            self.move()
            steps += 1
            if self.current_position is None:
                self.current_position = (0, 0)
        print("\nFinal room state:")
        self.display_room()

# Run the room cleaner agent
agent = RoomCleanerAgent()
agent.run()