from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def search_web(query: str):
    '''Searches the web and returns the results'''
    search_tool = DuckDuckGoSearchResults(num_results = 10, verbose= True)
    return search_tool.run(query)