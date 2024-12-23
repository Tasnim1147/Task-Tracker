import json
from time import strftime, localtime
from TaskTracker.status import TaskState

class Task(object):
   def __init__(
         self,
         id: int,
         description: str,
         createdAt: str = "",
         updatedAt: str = "",
         status: TaskState = TaskState.TODO,
      ) -> None:

      self.id = id
      self.description = description
      self.status = status
      if (not createdAt):
         self.createdAt = strftime("%a, %d %b %Y %H:%M", localtime())
      else:
         self.createdAt = createdAt
      if (not updatedAt):
         self.updatedAt = self.createdAt
      else:
         self.updatedAt = updatedAt


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
      return f"Task {self.id} ({self.status}): {self.description}"
   
   

class TaskJSONEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, Task):
         return {
               "id": obj.id,
               "status": str(obj.status),
               "description": obj.description,
               "createdAt": obj.createdAt,
               "updatedAt": obj.updatedAt
         }
      return super().default(obj)
   
class TaskJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if "id" in obj and \
           "status" in obj and \
            "description" in obj and \
            "createdAt" in obj and \
            "updatedAt" in obj:
            return Task(id=obj["id"], 
                        status=obj["status"],
                        description=obj["description"],
                        createdAt=obj["createdAt"],
                        updatedAt=obj["updatedAt"])
        return obj


