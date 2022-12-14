# PS

from cl_ht import Habits, Completion
from db import get_db, create_tables, add_habit, add_check, add_timespan, get_habit_names
from analyse import return_all_timespans, return_habits, return_longest_streak


class TestHabit:
    """Test habit tracker."""

    def setup_method(self):
        """Setup test database and test db functionalities"""
        self.db = get_db("test.db")
        create_tables(self.db)

    def test_db(self):
        add_timespan(self.db, "week", 7)
        add_timespan(self.db, "day", 1)
        add_habit(self.db, "test2", 1, 1)
        add_check(self.db, 1, 1)
        add_check(self.db, 1, 1)
        add_check(self.db, 1, 0)
        add_check(self.db, 1, 1)

    def test_habittracker(self):
        """Test Habittracker"""
        habit = Habits("test1", "week")
        Habits.deactivate_habit("test1")
        get_habit_names(self.db, 1)
        compl = Completion()
        Completion.check_habit(compl, "test1")

    def test_analyse(self):
        """Test analysis module"""
        return_habits(all=1)
        return_habits(timespan="week")
        return_all_timespans()
        streak = return_longest_streak(timespan="week")
        if streak == 6: print ("Proof. Habit calculation works.")
        streak = return_longest_streak(habitname="Jogging")
        if streak == 6: print ("Proof. Habit calculation works.")

    def teardown_method(self):
        pass
