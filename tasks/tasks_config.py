
TASK_CONFIGS = [
    {
        'name': 'location_task',

        'description': """This task involves comprehensive data collection process to provide
        the traveler with essential information when traveling from {from_city} to {to_city}, 
        between {from_date} to {to_date}. Gather information about accommodations,weather, 
        and events.""",

        'expected_output': """A detailed markdown report for {to_city} with list of recommended
        places to stay, weather, events and travel advisories.""",

        'agent' : 'location_expert',
        'output_file': 'location_report.md'
    },
    {
        'name': 'guide_task',

        'description': """Tailored to the traveler's interests like ({interests}), this task 
        focuses on creating a guide to cultural landmarks, food spots, activities, and events 
        in the {to_city}. The guide also highlights seasonal events and festivals that might 
        be of interest during the traveler's visit.""",

        "expected_output": """An interactive markdown guide for {to_city} personalized to the 
        traveler's interests.""",

        "agent": "guide_expert",
        "output_file": "guide_report.md"
    },
    {
        'name': 'planner_task',

        'description': """Using the collected location report and guide report, create a complete 
        day-by-day travel plan for {to_city}. Ensure that each day includes 3 or 4 activities based 
        on user's interests ({interests}), recommended places from location report, and guide report  
        based on availability between {from_date} and {to_date}. Output must be a daily 
        itinerary in markdown format with day headings (Day 1, Day 2, etc.)""",
        
        "expected_output": """A rich markdown document introducing {to_city} and a detailed day-by-day 
        travel plan covering {from_date} to {to_date}.""",
        
        "agent": "planner_expert",
        "output_file": "travel_plan.md",
        "context": ["location_task", "guide_task"] 
    }

]