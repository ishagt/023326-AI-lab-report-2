# Q1. Implement automated vacuum cleaner reflex agent.
import random
from typing import Self
class VacuumCleanerAgent:
    def __init__(self, room_size=2): #constructor
        self.room_size=room_size
        self.room = [[random.choice([0,1]) for _ in range(room_size)]
             for _ in range(room_size)]

#created room with random dirt (1=dirty, 0=clean)
# Random starting position
        self.position=(random.randint(0,room_size-1),random.randint(0,room_size-1))
# display room state
    def display_room(self):
        for i in range(self.room_size):
            for j in range(self.room_size):
                if (i,j)==self.position:
                    print("A",end=" ") # A represents the agent
                else:
                    print(self.room[i][j],end=" ")
            print()
        # perceive current state
    def perceive(self):
        x,y=self.position
        return self.room[x][y]
#simple reflex agent action
    def act(self):
        x,y=self.position
        if self.perceive()==1: #if dirty
            print(f"cell ({x},{y}) is dirty. Cleaning...")
            self.room[x][y]=0 #clean the cell
        else:
            print(f"cell ({x},{y}) is clean. Moving...")
            self.move()
            #move to a random adjacent cell
    def move(self):
        x,y=self.position
        possible_moves=[]
        if x>0:
            possible_moves.append((x-1,y)) #up
        if x<self.room_size-1:
            possible_moves.append((x+1,y)) #down
        if y>0:
            possible_moves.append((x,y-1)) #left
        if y<self.room_size-1:
            possible_moves.append((x,y+1)) #right
        self.position=random.choice(possible_moves)
        # Run the agent for a number of steps
    def run(self,steps=10):
        print("Initial room state:")
        for step in range(steps):
            print(f"\nStep {step+1}:")
            self.display_room()
            self.act()
        print("\nFinal room state:")
        self.display_room()

 # Run the vacuum cleaner agent 
agent=VacuumCleanerAgent(room_size=2)
agent.run(steps=10)