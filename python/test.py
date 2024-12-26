import logging
import time
from subprocess import PIPE, Popen
import typing
logging.basicConfig(filename="cli.log",
                    level=logging.INFO)


class TestTaskTracker(object):

    def __init__(self):
        self.file_name = "main.py"
        self.prompt = "task-cli "
        self.logger = logging.getLogger(self.prompt)
        self.process = Popen(["python", self.file_name], 
                             stdin=PIPE, 
                             stdout=PIPE, 
                             stderr=PIPE, 
                             text=True)

    def readline(self) -> str:
        line = ""
        while self.process.stdout.readable():
            char = self.process.stdout.read(1)
            if char == '\n' or not char: break
            line += char
            if line == self.prompt: break

        return line

        


    def process_io(self,
                   input_text: str
                   ) -> str:
        time.sleep(0.5)
        out = []
        self.logger.info("Starting to clean stdout")
        while True:
            if (self.process.stdout.readable()):
                line = self.readline()
                self.logger.info("Found: " + line)
                if (line.strip() == self.prompt.strip()): break
            else:
                break
            time.sleep(0.5)
            print("Continuing to clean stdout stream")
        self.logger.info(f"Starting to send input: {input_text}")
        self.process.stdin.write(input_text + '\n')
        self.process.stdin.flush()
        self.logger.info(f"Starting to read output")
        while True:
            if (self.process.stdout.readable()):
                out.append(self.readline())
                if (out[-1].strip() == self.prompt.strip()): 
                    break
            else:
                break

        self.logger.info(f"Input='{input_text}'")
        self.logger.info(f"Output='{out}'")
        return out

    def test_add(self): 
        for task in [
            "Buy groceries",
            "Brush teeth",
            "Eat lunch",
        ]:
            command = f"add {task}"
            self.process_io(input_text=command)

    def test_update(self): pass
    def test_delete(self): pass
    def test_mark_done(self): pass
    def test_mark_in_progress(self): pass
    def test_list(self): pass
    def test_list_done(self): pass
    def test_list_todo(self): pass
    def test_list_in_progress(self): pass
    def test_exit(self):
        self.process_io(input_text="exit")



    def test_all(self):
        self.test_add()
        self.test_update()
        self.test_delete()
        self.test_mark_done()
        self.test_mark_in_progress()
        self.test_list()
        self.test_list_done()
        self.test_list_in_progress()

        self.process.kill()






if __name__ == "__main__":
    tester = TestTaskTracker()
    tester.test_all()
        



        