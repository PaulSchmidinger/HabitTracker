# HabitTracker

A habit tracker is a list where you keep track of whether you have done something in a day, such as made your bed, do sports or drunk enough water.
This is the backend of a Habit Tracker, for the course "Object Oriented and Functional Programming with Python" (DLBDSOOFPP01).

## Installation
For installation use these two commands:

```shell
pip install -r requirements.txt
python install.py
```

## Useage
Start

```shell
python main.py
```

and follow the instructions on screen.

The CLI has the following main commands:
 - create_habit: This command is used to create a habit.
 - dea_habit: This command is used to deactivate a specified habit.
 - check: This command is used to check a specified habit.
 - habits: This command is used to get a list of all habits.
 - longest_streak: This command is used to get the longest streak. You have to either specify a habit or a timespan.
 - timespans: This command is used to get a list of all specified timespans.

 For further information on the main commands, please use "--help".


## Testing

This Habit Tracker can be tested with pytest and includes three test suites.

```shell
pytest .
```