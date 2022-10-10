from datetime import datetime
from db import add_habit, add_check, add_timespan, get_habits_data

class habits:
    def __init__(self, name:str, timespan:str):
        self.name = name
        self.created_t = datetime.now()
        self.active = True

        if timespan.lower() == "week":
            self.timespan = 1
        elif timespan.lower() == "day":
            self.timespan = 2
        else:
            raise Exception("Only 'week' and 'day' is possible!")

    def deactivate_habit(self):
         self.active = False

    def __store_habit(self, db):
        add_habit(db, self.name, self.active, self.timespan)

class completion:
    def __init__():
        pass

    def check (self, name:str):
        self.habit_name = name
            def __add_check(self, db)

    def streak(self, habit_id:int):
        