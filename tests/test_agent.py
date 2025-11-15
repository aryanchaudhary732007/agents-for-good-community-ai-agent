import unittest
from agents.community_agent import CommunityAgent

class TestCommunityAgent(unittest.TestCase):
    def test_issue_analysis(self):
        agent = CommunityAgent(api_key="dummy")
        result = agent.analyze_issue("garbage problem")
        self.assertIn("action_plan", result)

if __name__ == "__main__":
    unittest.main()

