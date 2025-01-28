# This library implements functionality of FRAgPLEnvironmentUtils.pl in python

from AgentClass import Agent

_env_pointer = None # Global variable for storing the base environment from which clones may be done

# Register an environment
def register_environment(env_obj):
    global _env_pointer
    _env_pointer = env_obj
    return _env_pointer

# Register a clone of an environment
def register_clone(candidate_clone):
    for clone in _env_pointer.get_clones():
        if candidate_clone == clone.get_name():
            return
     
    new_clone = (candidate_clone, True)
    _env_pointer.append_clone_env(new_clone)

# Returns a value of a fact in an environment
def query_environment(env_name:str, name_of_fact:str) -> list:
    global _env_pointer
    target_env = get_environment_by_name(env_name)
    #target_agent:Agent = locate_agent(agent)
    #assert that target_agent is in target_env?
    return target_env.get_fact_value(name_of_fact)

# Retutns environment with a given name if it exists
def get_environment_by_name(name:str):
    global _env_pointer
    root_env = _env_pointer
    if root_env.get_name() == name:
        return root_env
    else:
        for clone_env in root_env.get_clones():
            if clone_env.get_name() == name:
                return clone_env
    return None

# Places agent in an environment
def situate_agent_env(agent:str, env:str) -> Agent:
    target_env = get_environment_by_name(env)
    return target_env.create_and_situate_agent(agent_name=agent)
    
# Locates agent with a given name in environment
def locate_agent(agent_name:str, env):
    for ag in env.get_agents():
        if ag.get_name() == agent_name:
            return ag

    return None