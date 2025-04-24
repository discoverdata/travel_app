from crewai import Task
from tasks.tasks_config import TASK_CONFIGS
from agents.agents import agents


def create_tasks(trip_info, agent):
    """
    Create tasks dynamicaly based on user input from streamlit
    
    Arguments:
        trip_info (dict): user travel details
        agent: pre created agent
    
    """

    tasks = {}
    # First pass: create all tasks
    for config in TASK_CONFIGS:
        description = config['description'].format(**trip_info)
        tasks[config['name']] = Task(
            description = description,
            expected_output = config['expected_output'],
            agent = agents[config['agent']],
            output_file = config['output_file']
        )

    # Second pass: link context if needed 
    for config in TASK_CONFIGS:
        if 'context' in config:
            tasks[config['name']].context = [tasks[ctx_name] for ctx_name in config['context']]
    
    return tasks