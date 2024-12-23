from TaskTracker.task import Task, TaskJSONEncoder
from json import loads, dumps


def loadTasks(path: str) -> list[Task]:
    with open(path, 'r') as fd:
        return loads(fd.read())
    
def dumpTasks(
        path: str, 
        taskQueue: list[Task]
        ) -> None:
    with open(path, 'w') as fd:
        fd.write(dumps(taskQueue, cls=TaskJSONEncoder, indent=2))

