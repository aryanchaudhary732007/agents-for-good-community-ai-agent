import json
from utils.helpers import clean_text

class CommunityAgent:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def analyze_issue(self, issue: str) -> dict:
        """
        Takes a community issue and returns a structured plan.
        """

        issue = clean_text(issue)

        response = {
            "issue": issue,
            "causes": [
                "Lack of awareness",
                "Poor infrastructure",
                "Limited public participation"
            ],
            "action_plan": [
                "Organize awareness drives",
                "Deploy volunteers for surveys",
                "Coordinate with local authorities",
                "Provide community monitoring tools"
            ],
            "required_tools": [
                "Data collection forms",
                "Awareness posters",
                "Python-based analysis scripts"
            ]
        }

        return response

    def generate_python_script(self, problem: str) -> str:
        """
        Generates a safe Python script for data analysis or monitoring.
        """

        script = f'''
import pandas as pd

# Auto-generated community helper script
# Problem Focus: {problem}

def analyze_data(csv_file):
    df = pd.read_csv(csv_file)
    print("Columns:", df.columns)
    print("Basic Stats:")
    print(df.describe())

if __name__ == "__main__":
    print("Community Problem: {problem}")
    analyze_data("community_data.csv")
'''
        return script

