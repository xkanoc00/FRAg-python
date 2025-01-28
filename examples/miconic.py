# Class implementing miconic environment in python

import sys
import os
import random


# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EnviroClass import *

# Child class of Environment class
class Miconic(Environment):
    def __init__(self, name:str):
        super().__init__(name=name, clone=False)
        self.use_real_time = False # Either real_time or sim_time

        self.static_facts = {
            "LOWEST_FLOOR": 0,
            "HIGHEST_FLOOR": 100
        }

        # some facts here like 'traveled_distance' will be moved to agent's beliefe base
        self.dynamic_facts = {
            # These should be moved to agents belief after initialization
            # Related functions and methods reworked to accomodate that
            # Right now only one agent can be in the environment
            "traveled_distance": 0,
            "lift_at": 0,
            "transporting": 0,
            #------------------------
            "served": 0,
            "simulated_agents" : 0,
            "all_served": False,
            "tasks": [('Xander', 95, 66, 'waiting'),
                ('Zane', 7, 60, 'waiting'),
                ('Caleb', 17, 5, 'waiting'),
                ('Wendy', 44, 21, 'waiting'),
                ('David', 4, 30, 'waiting'),
                ('Frank', 76, 83, 'waiting'),
                ('Frank', 43, 58, 'waiting'),
                ('Victor', 75, 15, 'waiting'),
                ('Frank', 9, 65, 'waiting'),
                ('Xander', 75, 83, 'waiting'),
                ('David', 44, 83, 'waiting'),
                ('Paul', 83, 40, 'waiting'),
                ('Wendy', 22, 5, 'waiting'),
                ('Oscar', 18, 9, 'waiting'),
                ('Paul', 6, 30, 'waiting'),
                ('Bobby', 74, 94, 'waiting'),
                ('Jack', 99, 37, 'waiting'),
                ('David', 28, 90, 'waiting'),
                ('Rose', 23, 46, 'waiting'),
                ('Wendy', 64, 44, 'waiting'),
                ('Tina', 15, 57, 'waiting'),
                ('Mona', 47, 91, 'waiting'),
                ('Jack', 95, 28, 'waiting'),
                ('Steve', 96, 30, 'waiting'),
                ('Nancy', 25, 95, 'waiting'),
                ('Helen', 73, 59, 'waiting'),
                ('Tina', 14, 81, 'waiting'),
                ('Caleb', 89, 84, 'waiting'),
                ('Steve', 47, 76, 'waiting'),
                ('Uma', 97, 64, 'waiting'),
                ('Yara', 23, 16, 'waiting'),
                ('Zane', 41, 89, 'waiting'),
                ('Karen', 64, 15, 'waiting'),
                ('David', 23, 19, 'waiting'),
                ('Tina', 49, 36, 'waiting'),
                ('Alice', 97, 4, 'waiting'),
                ('Karen', 82, 84, 'waiting'),
                ('Oscar', 70, 95, 'waiting'),
                ('Leo', 48, 0, 'waiting'),
                ('Xander', 22, 48, 'waiting'),
                ('Bobby', 82, 22, 'waiting'),
                ('Karen', 27, 62, 'waiting'),
                ('David', 22, 71, 'waiting'),
                ('Frank', 43, 96, 'waiting'),
                ('Wendy', 92, 30, 'waiting'),
                ('Zane', 89, 18, 'waiting'),
                ('Karen', 21, 47, 'waiting'),
                ('Helen', 88, 71, 'waiting'),
                ('Leo', 76, 3, 'waiting'),
                ('Uma', 24, 17, 'waiting'),
                ('Ivy', 71, 17, 'waiting'),
                ('Oscar', 57, 92, 'waiting'),
                ('Helen', 91, 74, 'waiting'),
                ('Zane', 82, 1, 'waiting'),
                ('Garry', 83, 20, 'waiting'),
                ('Steve', 52, 21, 'waiting'),
                ('Victor', 46, 77, 'waiting'),
                ('Oscar', 25, 10, 'waiting'),
                ('Jack', 76, 29, 'waiting'),
                ('Frank', 89, 5, 'waiting'),
                ('Uma', 59, 28, 'waiting'),
                ('Tina', 65, 57, 'waiting'),
                ('Frank', 67, 4, 'waiting'),
                ('Caleb', 78, 5, 'waiting'),
                ('Mona', 12, 35, 'waiting'),
                ('Frank', 54, 79, 'waiting'),
                ('Ivy', 65, 76, 'waiting'),
                ('Rose', 81, 88, 'waiting'),
                ('Victor', 81, 3, 'waiting'),
                ('Zane', 57, 98, 'waiting'),
                ('Oscar', 37, 58, 'waiting'),
                ('Xander', 44, 99, 'waiting'),
                ('Helen', 8, 47, 'waiting'),
                ('Oscar', 97, 85, 'waiting'),
                ('Bobby', 36, 84, 'waiting'),
                ('Yara', 16, 86, 'waiting'),
                ('Wendy', 5, 81, 'waiting'),
                ('Zane', 49, 83, 'waiting'),
                ('Xander', 59, 28, 'waiting'),
                ('Erica', 52, 92, 'waiting'),
                ('Xander', 56, 51, 'waiting'),
                ('Yara', 96, 35, 'waiting'),
                ('David', 30, 14, 'waiting'),
                ('Zane', 58, 57, 'waiting'),
                ('Yara', 71, 40, 'waiting'),
                ('David', 22, 29, 'waiting'),
                ('Oscar', 54, 50, 'waiting'),
                ('Xander', 61, 67, 'waiting'),
                ('David', 48, 86, 'waiting'),
                ('Paul', 41, 33, 'waiting'),
                ('Leo', 77, 53, 'waiting'),
                ('Alice', 67, 92, 'waiting'),
                ('Steve', 39, 17, 'waiting'),
                ('Helen', 17, 84, 'waiting'),
                ('Frank', 47, 59, 'waiting'),
                ('Victor', 99, 90, 'waiting'),
                ('Karen', 54, 17, 'waiting'),
                ('Rose', 37, 83, 'waiting'),
                ('Oscar', 69, 41, 'waiting'),
                ('Frank', 27, 9, 'waiting')
            ]
        }


    # Checks integrity of environment settings
    def check_init_conditions(self) -> None:
        low = self.static_facts.get("LOWEST_FLOOR")
        high = self.static_facts.get("HIGHEST_FLOOR")
        for task in self.dynamic_facts["tasks"]:
            assert (task[1] >= low[0] and task[1] <= high[0]), f"passenger: {task[0]} has origin on a floor that is outside of bounds: {task[1]}"
            assert (task[2] >= low[0] and task[2] <= high[0]), f"passenger: {task[0]} has destination on a floor that is outside of bounds: {task[2]}"
    

    # TODO: board, travel, exit_lift to be reworked to work with individual agents (lifts) in the environment
    # Allows passengers with this floor as a destination to exit and all passengers with this floor as an origin to board
    def board(self, agent:Agent) -> None:
        self.exit_lift(agent)
        for i, passenger in enumerate(self.dynamic_facts["tasks"]):
            if passenger[1] == self.dynamic_facts["lift_at"] and passenger[3] == "waiting":
                print(f"passenger {passenger[0]} boarding lift")
                self.dynamic_facts["tasks"][i] = (passenger[0], passenger[1], passenger[2], "traveling")
    
    # chooses a floor, this will be done with FRAg later
    def get_floor(self, agent:Agent) -> int:
        waiting_floors = [passenger[1] for passenger in self.dynamic_facts["tasks"] if passenger[3] == "waiting"]
        traveling_floors = [passenger[2] for passenger in self.dynamic_facts["tasks"] if passenger[3] == "traveling"]
        all_possible_floors = waiting_floors + traveling_floors
        
        if all_possible_floors:
            return random.choice(all_possible_floors)
        # If no tasks are available, don't move
        return self.dynamic_facts["lift_at"]

    # Move the lift
    def travel(self, agent:Agent, destination:int) -> None:
        self.dynamic_facts["traveled_distance"] += abs(self.dynamic_facts["lift_at"] - destination)
        self.dynamic_facts["lift_at"] = destination

    # Allow passengers to exit the lift
    def exit_lift(self, agent:Agent) -> None:
        for i, passenger in enumerate(self.dynamic_facts["tasks"]):
            if passenger[2] == self.dynamic_facts["lift_at"] and passenger[3] == "traveling":
                print(f"passenger {passenger[0]} exiting lift")
                self.dynamic_facts["tasks"][i] = (passenger[0], passenger[1], passenger[2], "served")
                self.dynamic_facts["served"] += 1
                if self.dynamic_facts["served"] == len(self.dynamic_facts["tasks"]):
                    self.dynamic_facts["all_served"] = True

# Creates, registers and checks environment
# returns miconic if prolog program needs it
# if called like this:
#   py_call(miconic:'initialize_environment'(), Env), the Env has environment (Miconic) object
def initialize_environment():
    miconic:Miconic = Miconic("Miconic")
    # next function is optional
    # miconic.check_init_conditions()
    register_environment(env_obj=miconic) 
    miconic.check_init_conditions()
    return miconic
    # Possibly move the setup of model to a separate file?
    # Currently in initialization
    
