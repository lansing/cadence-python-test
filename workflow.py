import sys
import logging
from time import sleep

from cadence.activity_method import activity_method
from cadence.workerfactory import WorkerFactory
from cadence.workflow import workflow_method, Workflow, WorkflowClient

logging.basicConfig(level=logging.DEBUG)

TASK_LIST = "HelloActivity-python-tasklist"
DOMAIN = "sample_python"


# Activities Interface
class GreetingActivities:
    @activity_method(task_list=TASK_LIST, schedule_to_close_timeout_seconds=2)
    def compose_greeting(self, greeting: str, name: str) -> str:
        raise NotImplementedError


# Activities Implementation
class GreetingActivitiesImpl:
    def compose_greeting(self, greeting: str, name: str):
        return greeting + " " + name + "!"


# Workflow Interface
class GreetingWorkflow:
    @workflow_method(execution_start_to_close_timeout_seconds=10, task_list=TASK_LIST)
    async def get_greeting(self, name: str) -> str:
        raise NotImplementedError


# Workflow Implementation
class GreetingWorkflowImpl(GreetingWorkflow):

    def __init__(self):
        self.greeting_activities: GreetingActivities = Workflow.new_activity_stub(GreetingActivities)

    async def get_greeting(self, name):
        return await self.greeting_activities.compose_greeting("Hello", name)
