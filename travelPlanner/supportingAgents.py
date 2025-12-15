from google.adk.agents import Agent
from travelPlanner.tool import google_search_grounding
from travelPlanner.tool import  location_search_tool
from google.adk.tools import AgentTool
from google.adk.tools import FunctionTool

LLM = "gemini-2.0-flash-001"

news_agent = Agent(
    model = LLM,
    name = "news_agent",
    description = "Suggest key travel events and news; uses search for current info.",
    instruction = """
                You are responsible for provding a  list of events and news recommendations based on the user's query.
                Limit the choices to 10 results. You need to use google_search_grounding agent to search the web for information.
                """,

    tools = [google_search_grounding]
)
places_agent = Agent(
    model = LLM,
    name = "place_agent",
    description = "Suggest location based on the user preferences.",
    instruction = """
                You are responsible for makin suggestions on actual places based on the user's query.
                Limit the choices to 10 results.
                Each place must have name, location and address.
                You can use the location_search_tool to find latitude and longitude of the place and address.
                """,

    tools = [location_search_tool]
)

travel_inpiration_agent = Agent(
    model = LLM,
    name = "travel_inspiration_agent",
    description = "Inspires users with new travel ideas.",
    instruction = """
                You are travel inspiration agent who helps users find their next big dream vacations destinations.
                Your role and goal is to help the user to identify the destination and a few activites at the destination the user is interested.
                
                As part of that, user many ask you for general history and knowledge about the destination, in that scenario you should provide the information in concise manner:
                - You will call the two agent tools `place_agent(inspiration query)` and `news_agent(inspiration query)` when appropriate:
                IMPORTANT TOOL RULES:
                - If the user asks for ANY information that is current, real-time, date-specific, event-specific, or fact-based,
                  you MUST NOT answer directly.
                - Instead, you MUST call the appropriate sub-agent tool:
                    • Call `news_agent` for events, dates, schedules, real-time info, history.
                    • Call `place_agent` for places, locations, addresses, coordinates.
                
                STRICT DELEGATION RULE:
                - Do NOT answer from your own knowledge if the answer depends on real-time or factual data.
                - ALWAYS delegate to news_agent or place_agent first when relevant.
                - Only provide a direct LLM answer if the user is asking for general opinions or inspiration (not facts).
                
                EXAMPLES:
                - “Suggest me the Real Madrid match date in December” → MUST call news_agent.
                - “Tell me cafes near the Eiffel Tower” → MUST call place_agent.
                - “Give me ideas for a relaxing beach vacation” → You MAY answer directly.

                AFTER TOOL RESPONSES:
                - Combine results into a short, natural human-like summary.
                - Present the info clearly in bullet points.
                - Add 1–2 helpful suggestions like:
                  “Would you like me to find hotels near the stadium?”
                  “Do you want me to plan a 2-day itinerary for Madrid?”
                
                FAILURE CONDITION:
                - If you answer something like ‘I don’t have access to real-time data,’ it means you FAILED to use tools.
                Tone rules:
                - Write naturally like a travel concierge.
                - Be helpful and proactive.
                - Never be robotic.
                                
                
                     """,


    tools= [AgentTool(agent = news_agent), AgentTool(agent = places_agent)]
    # - Use `news_agent` to provide key events and news recommendations based on the user's query.
                # - Use `place_agent` to provide a list of information or nearby places to famous locations when user asks fot it.

             
    )
