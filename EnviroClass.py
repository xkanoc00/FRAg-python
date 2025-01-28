# This class implements general environment from which specific environments inherit

from AgentClass import Agent
from EnvironmentUtils import *

class Environment:
    def __init__(self, name:str, clone:bool):
        self.name = name # description/name
        self.clones: list[self:Environment] = [] # List of clones of environments
        self.agents: list[Agent] = []       # List of agents situated in the environment
        #self.actions: list = []            # List of actions, could be used for replays later?
        # ! static_facts HAVE TO BE UPPERCASE 
        self.static_facts = {}              # Dictionary of static facts about the environment
        self.dynamic_facts = {}             # Dictionary of dynamic facts about the environment
        self.clone = clone  





# FACTS ----------------------------------------------------------------

    def add_facts(self, facts: dict) -> None:
        for (fact_name, value) in facts:
            if fact_name not in self.dynamic_facts:
                self.dynamic_facts[fact_name] = value
    
    
    def update_fact_value(self, key:str, new_value) -> None:
        if self.dynamic_facts[key]:
            self.dynamic_facts[key] = new_value
        # Static facts cannot be modified at runtime

    


# AGENT --------------------------------------------------------------

    # add beliefs to all agents
    def add_beliefs_agents(self, agent_names:list[str], keys:list[str], values:list) -> None:
        for agent in agent_names:
            ag:Agent = locate_agent(agent, self)
            ag.add_beliefs_agent(keys, values)


    # Register agent with the environment and vice versa
    def append_agent(self, agent:Agent) -> None:
        self.agents.append(agent)
        agent.set_env(self)


    # Register environment's clone with the environment  
    def append_clone_env(self, env) -> None:
        self.clones.append(env)


    # Creates and situates agent in this environment
    def create_and_situate_agent(self, agent_name:str) -> Agent:
        new_agent = Agent(agent_name)
        if new_agent not in self.get_agents():
            self.append_agent(new_agent)
            return new_agent


    # Sets up agent's beliefs, copying the facts from situated environment
    def init_agent_beliefs(self, agent_name:str) -> None:
        agent:Agent = self.agents[agent_name] # Check if agent is in the main env
        if agent is None: # Else check every clone env for a clone with that name
            for clone in self.clones:
                agent = clone.agents[agent_name]
                if agent is not None:
                    break
        assert agent is not None, f"Agent {agent_name} DNE" # Assert some agent was found
        agent.init_beliefs()


    # Sets up beliefs for all supplied agents
    def init_agents_beliefs(self, agent_names:list[str]) -> None:
        for agent in agent_names:
            self.init_agent_beliefs(agent)


    def situate_agent(self, agent:Agent) -> None:
        if agent not in self.get_agents():
            self.agents.append(agent)


    # Situate agent in clone of this environment
    def situate_agent_cloned_env(self, agent:Agent, clone_name:str) -> None:
        for clone in self.clones:
            if clone.get_name() == clone_name:
                clone.agents.append(agent)
    





    # GETTERS-------------------------------------------
    # Return name of 
    def get_name(self) -> str:
        return self.name

    # Return all environment clones
    def get_clones(self) -> list:
        return self.clones
    
    # Return all agent objects
    def get_agents(self) -> list[Agent]:
        return self.agents

    # Return names of all agents
    def get_names_a(self) -> list:
        names = []
        for a in self.get_agents():
            names.append(a.get_name())
        return names
    
    # Find and return agent by its name in the environment
    def get_agent_by_name(self, agent_name:str) -> Agent:
        for agent in self.agents:
            if agent.get_name() == agent_name:
                return agent

    # Query environment for a value of a given fact name
    def get_fact_value(self, key:str):
        if key in self.dynamic_facts:
            return self.dynamic_facts[key]
        # Check if the key exists in static_facts
        elif key in self.static_facts:
            return self.static_facts[key]
        # Key not found in either dictionary
        else:
            return None
        



    # DEBUG----------------------------------------------
    def status_report(self) -> str | None:
        print ("Static facts:")
        print (self.static_facts)
        print ("Dynamic facts")
        print (self.dynamic_facts)
        print ("Agents:")
        for agent in self.agents:
            print (agent.get_name(),":")
            print (agent.get_beliefs())
        print()