from travelPlanner.agent import root_agent

def main():
    print("Hello! I am your travel planning assistant. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = root_agent.invoke(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()
