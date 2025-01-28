# This class implements agent and its behavior towards environment

class Agent:
    def __init__(self, name:str):
        self.name = name
        self.env = None
        self.static_dynamic_divide:int = 0
        self.beliefs = {}

    # add a belief to agent
    def add_beliefs_agent(self, keys:list, values:list) -> None:
        if len(keys) != len(values):
            raise ValueError("Keys and values lists must have the same length")

        for key, value in zip(keys, values):
            if key not in self.beliefs:
                self.beliefs[key] = value


    # TODO check if 
    # Deletes all dynamic facts
    def delete_belief_base(self):
        keys = list(self.beliefs.keys())  # Get list of keys/facts
        for key in keys:
            if key.islower():  # Check if the fact is dynamic (lowercase)
                del self.beliefs[key]


    # Returns name of agent
    def get_name(self) -> str:
        return self.name


    # Sets environment agent will be acting in
    def set_env(self, env):
        self.env = env


    # Updates agents belief base
    def update_belief_base(self): 
        self.delete_belief_base
        self.get_belief_base


    # Returns environment in which agent is placed
    def return_environment(self):
        return self.env


    # Gets dynamic facts
    def get_belief_base(self):
        for key, value in self.env.dynamic_facts.items():
            self.beliefs[key] = value


    # Sets up initial belief base - both static and dynamic facts
    def init_beliefs(self):
        for key, value in self.env.static_facts.items():  # Use .items() to unpack key-value pairs
            self.beliefs[key] = value
            self.static_dynamic_divide += 1
        self.get_belief_base()


    # return agents beliefs
    def get_beliefs(self) -> list:
        return self.beliefs
    

    # Prints all relevent 
    def status_report(self):
        print("AGENT:")
        print(self.name)
        print(self.env)
        print(self.static_dynamic_divide)
        print(self.beliefs)
        print()