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

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
        self.manager = TaskManager()

    def do_help(self, arg):
        """Override help command to display custom help."""
        if arg:
            # Show custom help for a specific command
            method_name = "help_" + arg.replace("-", "_")
            method = getattr(self, method_name, None)
            if method:
                method()
            else:
                print(f"No help available for '{arg}'.")
        else:
            # Default behavior to show available commands
            print("Available commands:")
            for name in self.get_names():
                if "do_" == name[:3]:
                    command = name[3:]
                    if "mark" in command:
                        print(f"- {command.replace("_", "-")}")
                    else:
                        print(f"- {command}")
    
    def do_exit(self, _):
        """Exit the application"""
        print("Goodbye!")
        return True

    def default(self, line):
        """Handle unrecognized commands."""
        if "mark" in line:
            method_name = "do_" + line.replace("-", "_")
            method = getattr(self, method_name, None)
            if method:
                method(line)
                return
        print(f"Unknown command: {line}. Type 'help' for a list of commands.")

    # Main functionalities

    def do_add(self, arg):
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



def main():
    # print('Hello, world!')
    TaskCLI().cmdloop()

if __name__ == "__main__":
    main()