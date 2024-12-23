from enum import Enum

class TaskState(Enum):
    TODO = "TODO"
    INPROGRESS = "IN PROGRESS"
    DONE = "DONE"

    def __str__(self):
        return self.value
    