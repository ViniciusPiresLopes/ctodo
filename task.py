NEW = 0
DONE = 1
REMOVE = 2


class Task:
    def __init__(self, text):
        self.text = text
        self.state = NEW
    
    def is_done(self):
        if self.state == DONE:
            return True

        return False

    def show_task(self):
        if self.is_done():
            print(f"[x] {self.text}")
        else:
            print(f"[ ] {self.text}")
