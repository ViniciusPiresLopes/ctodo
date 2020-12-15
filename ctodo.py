from task import Task, NEW, DONE, REMOVE
import os, platform

# Verifies platform for using the right clear command
if platform.system() == "Windows":
    CLEAR_COMMAND = "cls"
else:
    CLEAR_COMMAND = "clear"

# Constants
DIGITS = "0123456789"
EXIT = "exit"
CLEAR_LIST = "clear"


# Main class
class CTodo:  # CTodo -> Console To Do (List)
    def __init__(self):
        self.todo_tasks = []
        self.answer = ""
        self.running = True

    def clear(self):
        """
        Clear the console.
        """
        os.system(CLEAR_COMMAND)

    def show_title(self):
        """
        Shows a beautiful title with the program's name.
        """
        print("=" * 30)
        print(f"{'Console To Do List':^30}")
        print("=" * 30)
    
    def show_sep(self, symbol="-", qt=30):
        """
        Prints a line of qt chars with one symbol, a separator.
        :qt -> quantity of chars
        """
        print("-" * qt)

    def show_data(self):
        """
        Show the todo list data in an beautiful way.
        """
        for i, task in enumerate(self.todo_tasks):
            print(f"{i + 1}° - ", end="")
            task.show_task()
    
    def is_str_int(self, string):
        is_number = True
        for char in string:
            if char not in DIGITS:
                is_number = False
        
        return is_number
    
    def input(self):
        """
        Ask things to user.
        """
        self.answer = str(input("Type new task or task index to finish it: ")).strip()

    def logic(self):
        """
        Process input datas.
        """
        if self.answer == "": return

        if self.is_str_int(self.answer):
            self.answer = int(self.answer)

            if self.answer < 1 or self.answer > len(self.todo_tasks):
                pass
            else:
                self.todo_tasks[self.answer - 1].state += 1

                if self.todo_tasks[self.answer - 1].state == REMOVE:
                    self.todo_tasks.pop(self.answer - 1)
        else:
            if self.answer == EXIT:
                self.running = False
            elif self.answer == CLEAR_LIST:
                self.todo_tasks.clear()
            else: 
                self.todo_tasks.append(Task(self.answer))

    def update(self):
        try:
            self.clear()
            self.show_title()
            self.show_data()
            self.show_sep()

            self.input()
            self.logic()
        except KeyboardInterrupt:
            print()
            self.running = False
    
    def run(self):
        while self.running:
            self.update()
