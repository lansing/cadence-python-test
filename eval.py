import sys
import logging
from time import sleep

from cadence.activity_method import activity_method
from cadence.workerfactory import WorkerFactory
from cadence.workflow import workflow_method, Workflow, WorkflowClient

from workflow import GreetingActivitiesImpl, GreetingWorkflowImpl, GreetingWorkflow

logging.basicConfig(level=logging.DEBUG)

TASK_LIST = "HelloActivity-python-tasklist"
DOMAIN = "sample_python"


if __name__ == '__main__':
    print("creating client")
    client = WorkflowClient.new_client(domain=DOMAIN)
    print("creating workflow stub")
    greeting_workflow: GreetingWorkflow = client.new_workflow_stub(GreetingWorkflow)
    print("initializing workflow")
    result = greeting_workflow.get_greeting("Python")
    print(result)
