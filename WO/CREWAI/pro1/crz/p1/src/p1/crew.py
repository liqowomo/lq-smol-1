from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import SerperDevTool, ScraperWebsiteTool, FileWriterTool
from dotenv import load_dotenv

load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class P1:
    """P1 crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def retrieve_news(self) -> Agent:
        return Agent(
            config=self.agents_config["retrieve_news"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def website_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config["website_scraper"],
            tools=[ScraperWebsiteTool()],
            verbose=True,
        )

    @agent
    def ai_news_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["ai_news_writer"],
            tools=[],
            verbose=True,
        )

    @agent
    def file_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["file_writer"],
            tools=[FileWriterTool()],
            verbose=True,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def retrieve_news_task(self) -> Task:
        return Task(
            config=self.tasks_config["retrieve_news_task"],
        )

    @task
    def website_scraper_task(self) -> Task:
        return Task(
            config=self.tasks_config["website_scraper_task"],
        )

    @task
    def ai_news_write_task(self) -> Task:
        return Task(
            config=self.tasks_config["ai_news_write_task"],
        )

    @task
    def file_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config["file_writer_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the P1 crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )