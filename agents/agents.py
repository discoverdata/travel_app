from crewai import Agent
from tools.search_tool import search_web
from llm_setup import initialize_llm
from agents.agents_config import AGENTS_CONFIG
llm = initialize_llm()


def create_agent(name, role, goal, backstory):

    if name in ['guide_expert', 'location_expert']:
        tools = [search_web]
    else:
        tools = []
    
    return Agent(
        role = role,
        goal = goal, 
        backstory= backstory,
        tools = tools,
        verbose= True,
        max_iter= 5,
        llm= llm,
        allow_delegation= False

    )
# Create a dictionary of agents dynamically
agents = {config['name']:create_agent(config['name'], config['role'], config['goal'], config['backstory'])
          for config in AGENTS_CONFIG }