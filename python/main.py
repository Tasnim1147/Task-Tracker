import cmd
from TaskTracker.manager import TaskManager

def checkValidParameter(param: any,
                        t: type
                        ) -> bool:
    try:
        castedParam = t(param)
        return castedParam
    except:
        return False

class TaskCLI(cmd.Cmd):
    intro = "Welcome to the Task Tracking CLI. Type help or ? to list commands.\n"
    prompt = "task-cli "

    def __init__(self, 
                 completekey = "tab", 
                 stdin = None, 
                 stdout = None):
        super().__init__(completekey, stdin, stdout)

    def do_help(self, 
                arg: str
                ) -> None:
        """Override help command to display custom help."""
        if arg:
            if ("mark-done" in arg): arg = arg.replace('-', '_', 1)
            elif ("mark-in-progress" in arg): arg = arg.replace('-', '_', 2)
            super().do_help(arg)
        else:
            # Default behavior to show available commands
            # In case of mark_* replace '_' with '-'
            print("Available commands:")
            for name in self.get_names():
                if "do_" == name[:3]:
                    command = name[3:]
                    if "mark" in command:
                        print(f"- {command.replace("_", "-")}")
                    else:
                        print(f"- {command}")
    
    def do_exit(self, _) -> None:
        """Exit the application"""
        print("Goodbye!")
        return True

    def default(self, 
                line: str
                ) -> None:
        """Handle unrecognized commands."""
        if ("mark-in-progress" in line):
            new_line = line.replace('-', '_', 2)
            self.onecmd(new_line)
            return
        elif ("mark-done" in line):
            new_line = line.replace('-', '_', 1)
            self.onecmd(new_line)
            return
        print(f"Unknown command: {line}. Type 'help' for a list of commands.")

    # Handle mark-*

    # Main functionalities

    def do_add(self, 
               arg: str
               ) -> None:
        """Add a new task: add <task_description>"""
        if arg:
            task = self.manager.add(arg)
            print(f"Task added successfully (ID: {task.id})")
        else:
            print("Usage: add <task_description>")

    def do_update(self, 
                  arg: str
                  ) -> None:
        """Update a task: update <task_id> <task_description>"""
        if arg:
            args = arg.split(" ", maxsplit=1)
            taskId = checkValidParameter(args[0], int)
            if taskId:
                task = self.manager.update(taskId, args[1])
                if task:
                    print(f"Task updated successfully (ID: {task.id})")
                else:
                    print(f"Task doesn't exist (ID: {taskId})")
                return

        print("Usage: update <task_id> <task_description> ")

    def do_delete(self,
                  arg: str
                  ) -> None:
        """Delete a task: delete <task_id>"""
        if arg:
            taskId = checkValidParameter(arg, int)
            if taskId:
                task = self.manager.delete(taskId)
                if task:
                    print(f"Task deleted successfully (ID: {task.id})")
                else:
                    print(f"Task doesn't exist (ID: {taskId})")
                return

        print("Usage: delete <task_id>")

    def  do_mark_done(self,
                      arg: str
                      ) -> None:
        """Mark a task as done: mark-done <task_id>"""
        if arg:
            taskId = checkValidParameter(arg, int)
            if taskId:
                task = self.manager.markDone(taskId)
                if task:
                    print(f"Task marked successfully (ID: {task.id})")
                else:
                    print(f"Task doesn't exist (ID: {taskId})")
                return

        print("Usage: mark-done <task_id>")

    def  do_mark_in_progress(self,
                             arg: str
                             ) -> None:
        """Mark a task as in-progress: mark-in-progress <task_id>"""
        if arg:
            taskId = checkValidParameter(arg, int)
            if taskId:
                task = self.manager.markInProgress(taskId)
                if task:
                    print(f"Task marked successfully (ID: {task.id})")
                else:
                    print(f"Task doesn't exist (ID: {taskId})")
                return

        print("Usage: mark-in-progress <task_id>")

    def do_list(self,
                arg: str
                ) -> None:
        """List all the tasks: list
           List tasks with todo status: list todo
           List tasks with in progress status: list in-progress
           List tasks with done status: list done"""
        if not arg:
            self.manager.listAllTask()
        elif arg == "todo":
            self.manager.listTodoTask()
        elif arg == "in-progress":
            self.manager.listInProgressTask()
        elif arg == "done":
            self.manager.listDoneTask()
        else:
            print("Usage list <'todo' | 'in-progress' | 'done' | ''>")

    # Post loop
    def postloop(self):
        self.manager.dumpTasks()
        return super().postloop()
    
    # Pre loop
    def preloop(self):
        self.manager = TaskManager()
        return super().preloop()



def main():
    taskCLI = TaskCLI()
    taskCLI.cmdloop()

if __name__ == "__main__":
    main()