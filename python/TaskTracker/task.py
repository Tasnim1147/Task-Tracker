from time import strftime, localtime
from TaskTracker.status import TaskState

class Task(object):
   def __init__(
         self,
         id: int,
         description: str,
         status: TaskState
      ) -> None:

      self.id = id
      self.description = description
      self.status = status
      self.createdAt = strftime("%a, %d %b %Y %H:%M", localtime())
      self.updatedAt = self.createdAt


   def markInProgress(self) -> None:
      self.updatedAt = strftime("%a, %d %b %Y %H:%M", localtime())
      self.status = TaskState.INPROGRESS

   def markDone(self) -> None:
      self.updatedAt = strftime("%a, %d %b %Y %H:%M", localtime())
      self.status = TaskState.DONE

   def setDescription(
      self, 
      description: str
      ) -> None:
      self.updatedAt = strftime("%a, %d %b %Y %H:%M", localtime())
      self.description = description

   def __repr__(self) -> str:
      return f"Task {self.id} ({self.status}): {self.des}"

   


