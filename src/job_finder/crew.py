from dotenv import load_dotenv
load_dotenv()

import crewai.llms.cache as _crewai_cache

_crewai_cache.mark_cache_breakpoint = lambda msg: msg

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool


@CrewBase
class JobFinder:
    """Research and Job Finder Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            verbose=False,
            allow_delegation=False,
            llm=LLM(
                model="openrouter/openai/gpt-oss-120b:exacto",
                temperature=0,
            ),
        )

    @agent
    def job_finder(self) -> Agent:
        search_tool = SerperDevTool()

        return Agent(
            config=self.agents_config["job_finder"],
            tools=[search_tool],
            verbose=False,
            allow_delegation=False,
            max_iter=1,
            llm=LLM(
                model="openrouter/openai/gpt-oss-120b:exacto",
                temperature=0,
            ),
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def job_search_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_search_task"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )