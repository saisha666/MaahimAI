# tests/test_agents_playbook.py
import unittest
import subprocess
from maahimai import MaahimAI

class TestMaahimAIFramework(unittest.TestCase):
    def test_autogen_agents(self):
        maahimai = MaahimAI(agent_file='tests/autogen-agents.yaml')
        # result = maahimai.run()

    def test_crewai_agents(self):
        maahimai = MaahimAI(agent_file='tests/crewai-agents.yaml')
        # result = maahimai.run()

    def test_search_tool_agents(self):
        maahimai = MaahimAI(agent_file='tests/search-tool-agents.yaml')
        # result = maahimai.run()

    def test_inbuilt_tool_agents(self):
        maahimai = MaahimAI(agent_file='tests/inbuilt-tool-agents.yaml')
        # result = maahimai.run()