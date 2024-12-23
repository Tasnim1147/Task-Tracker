from typing import Callable, Union
from TaskTracker.task import Task
from TaskTracker.status import TaskState

class TaskManager(object):
    def __init__(
            self,
            home: str = "./"
            ):
        self.taskQueue: list[Task] = []
        self.taskCount: int = 1


    def _initializeTasks(self) -> None:
        pass

    def add(self,
            description: str
            ) -> Task:
        task = Task(self.taskCount, description)
        self.taskQueue.append(task)
        self.taskCount += 1
        return task
    
    def update(self,
               taskId: int,
               description: str
               ) -> Union[Task, None]:
        tasks = filter(lambda task : task.id == taskId, self.taskQueue)
        if len(tasks) == 0: return None
        else:
            task = tasks[0]
            task.setDescription(description)
            return task

    def _findTaskIndex(
                       self,
                       taskId: int,
                       ) -> int:
        for idx, task in enumerate(self.taskQueue):
            if (task.id == taskId): return idx

        return -1

    def delete(
               self,
               id: int,
               ) -> Union[Task, None]:
        index = self._findTaskIndex(id)
        if (index == -1): return None
        return self.taskQueue.pop(index)
    
    def markDone(
            self,
            taskId: int
    ) -> Union[Task, None]:
        for task in self.taskQueue:
            if (task.id == taskId):
                task.markDone()
                return task
        return None
    
    def markInProgress(
            self,
            taskId: int
    ) -> Union[Task, None]:
        for task in self.taskQueue:
            if (task.id == taskId):
                task.markInProgress()
                return task
        return None

    def _listTaskWithFilter(
            self,
            fn: Callable[[Task], bool],
            ) -> None:
        for task in filter(self.taskQueue, fn): print(task)

    def listDoneTask(self) -> None:
        self._listTaskWithFilter(lambda task: task.status == TaskState.DONE)
        
    def listInProgressTask(self) -> None:
        self._listTaskWithFilter(lambda task: task.status == TaskState.INPROGRESS)
        
    def listTodoTask(self) -> None:
        self._listTaskWithFilter(lambda task: task.status == TaskState.TODO)