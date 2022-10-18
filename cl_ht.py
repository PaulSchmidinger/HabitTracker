#PS

from db import get_db, add_habit, add_check, get_habit_id, update_deactiveate, get_habit_names, get_timespan_id, get_habits_timespan, get_habits_checks, get_streaks
from datetime import datetime

class habits:
    """Class that defines habits. Includes methods for creating and deactivating."""

    def __init__(self, name:str, timespan:str):
        """Initalizes a new habit. An active habit must have an unique name. Timespans have to be defined in the database, by default 'week' and 'day' are implemented. Checks, if entered name is already used for an active habit and, if the entered timespan is present in the database."""

        #Checks if entered name is already in the database.
        habit_names = get_habit_names(get_db(), 0)
        li_habit_names = []
        for all in habit_names: li_habit_names.append(all[0])
        if name in li_habit_names:
            raise Exception("Name already in database!")
        else:
            self.name = name      

        #Checks, if timespan is in the database
        self.timespan = get_timespan_id(get_db(), timespan=timespan)

        #Adds habit to database
        add_habit(get_db(), self.name, self.timespan)

        print ("Habit created!")

    def deactivate_habit(name):
        """Deactivates the given habit and saves it to the database."""
        habit_id = get_habit_id(get_db(),name)
        if type(habit_id) == str: return print(habit_id)
        update_deactiveate(get_db(), habit_id)
        
        print("Habit deactivated.") 


class completion:
    """Class, that defines the completion of habits."""

    def check_habit(self, name:str):
        """Checks a given habit. You can only check active habits."""
        self.name = name
        self.habit_id = get_habit_id(get_db(),self.name)
        if type(self.habit_id) == str: return print(self.habit_id)
        self.in_time, in_time_msg, streak_msg = self.__check_in_time()
        add_check(get_db(), self.habit_id, self.in_time)
        return print("Habit '"+self.name+"' checked! " + str(in_time_msg) + " " + str(streak_msg))

    def __check_in_time(self):
        """Checks, if the user has checked in or on time."""
        self.timespan_name, self.timespan_days = get_habits_timespan(get_db(),self.habit_id)
        
        #Calculation
        self.li_checks = get_habits_checks(get_db(), self.habit_id)
        if len(self.li_checks) == 0:
            date_time_last_check = datetime.today()
        else:
            date_time_last_check = datetime.strptime(self.li_checks[-1][0], '%Y-%m-%d %H:%M:%S')
        diff = datetime.now().date() - date_time_last_check.date()
        if int(diff.days) <= self.timespan_days:
            in_time = 1
            streak_msg = self.__streak()
            in_time_msg = "You have checked in time. Congratulations!!"
        else:
            in_time = 0
            in_time_msg = "Unfortunately you have not checked in time and broke the habit. Try harder!!"

        return in_time, in_time_msg, streak_msg

    def __streak(self):
        li_streaks = get_streaks(get_db(), self.habit_id)
        
        if len(li_streaks) == 0:
            streak_msg = "You have successfully established a streak of 1 periods! Super!"
            return streak_msg

        if self.li_checks[-1][1] == 1:
            periods = len(li_streaks)+1
            streak_msg = "You have successfully established a streak of " + str(periods) + " periods! Super!"
        
        return streak_msg