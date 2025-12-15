from google.adk.agents import Agent
from travelPlanner.supportingAgents import travel_inpiration_agent
LLM = "gemini-2.0-flash-001"
root_agent = Agent(
    model = LLM,
    name = "travel_planner_main",
    description= "A helpful travel planning assistant that help users plan their trips by providing information and suggest based on their preferences.",
    instruction= """
        - You are an exclusive travel concierge agent.
        - You help users to dicover their dream holiday destination and plan their vacation.
        -  Whenever the user asks anything that requires:
            • web search
            • finding hotels, cafes, attractions
            • trip planning
            • weather
            • news about a destination
            • itinerary creation
          → You MUST delegate that task to travel_inspiration_agent.
        - You can't use tool directly.
        """,

    sub_agents= [travel_inpiration_agent]    
        
    

)
