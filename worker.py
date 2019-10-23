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
    factory = WorkerFactory("localhost", 7933, DOMAIN)
    worker = factory.new_worker(TASK_LIST)
    worker.register_activities_implementation(GreetingActivitiesImpl(), "GreetingActivities")
    worker.register_workflow_implementation_type(GreetingWorkflowImpl)
    factory.start()
    print("worker started")