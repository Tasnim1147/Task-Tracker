import logging
from subprocess import PIPE, Popen

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

    def test_add(self): pass
    def test_update(self): pass
    def test_delete(self): pass
    def test_mark_done(self): pass
    def test_mark_in_progress(self): pass
    def test_list(self): pass
    def test_list_done(self): pass
    def test_list_todo(self): pass
    def test_list_in_progress(self): pass

    def test_all(self):
        self.test_add()
        self.test_update()
        self.test_delete()
        self.test_mark_done()
        self.test_mark_in_progress()
        self.test_list()
        self.test_list_done()
        self.test_list_in_progress()






if __name__ == "__main__":
    tester = TestTaskTracker()
    tester.test_all()
        



        