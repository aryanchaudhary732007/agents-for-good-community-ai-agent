from agents.community_agent import CommunityAgent
from config.config import API_KEY

def main():
    print("=== Community Helper AI Agent ===\n")
    
    issue = input("Enter a community problem: ")

    agent = CommunityAgent(api_key=API_KEY)

    result = agent.analyze_issue(issue)
    print("\nAnalysis Result:")
    print(result)

    print("\nGenerated Python Script Preview:")
    generated_script = agent.generate_python_script(issue)
    print(generated_script)

if __name__ == "__main__":
    main()

