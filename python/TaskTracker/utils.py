from TaskTracker.task import Task, TaskJSONEncoder, TaskJSONDecoder
from json import loads, dumps
import os

def loadTasks(path: str) -> list[Task]:
    if (not os.path.exists(path)): return []
    with open(path, 'r') as fd:
        return loads(fd.read(), cls=TaskJSONDecoder)
    
def dumpTasks(
        path: str, 
        taskQueue: list[Task]
        ) -> None:
    with open(path, 'w') as fd:
        fd.write(dumps(taskQueue, cls=TaskJSONEncoder, indent=2))

