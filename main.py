#PS

import click
from cl_ht import habits, completion
from analyse import return_all_timespans, return_habits, return_longest_streak

print("Welcome to the habit tracker backend.")

@click.group()
def cli():
    pass    

@cli.command(name='create_habit', help="This command is used to create a habit.")
@click.option('--name', type=str, help="Specify the name of the new habit.")
@click.option('--timespan', type=str, help="Specify the timespan of the new habit. If you are unsure which timespans exist, please use the command 'python main.py timespans'.")
def create_habit(name, timespan):
    habits(name=name, timespan=timespan)

@cli.command(name='dea_habit', help="This command is used to deactivate a specified habit.")
@click.option('--name', type=str, help="Specify the name of the habit, you want to deactivate.")
def dea_habit(name):
    habits.deactivate_habit(name)

@cli.command(name='check', help="This command is used to check a specified habit.")
@click.option('--name', type=str, help="Specify the name of the habit, you want to check.")
def check(name):
    compl = completion()
    compl.check_habit(name)

@cli.command(name='habits', help="This command is used to get a list of all habits.")
@click.option('--all', is_flag=True, help="Use this flag to specify, if you want the deactivated habits to be included.")
@click.option('--timespan', type=str, default="all", help="Specify a timespan, if you only want habits with a specified timespan included. Default: all")
def habits(all, timespan):
    if all:
        return_habits(all=1, timespan=timespan)
    else:
        return_habits(all=0, timespan=timespan)

@cli.command(name='longest_streak', help="This command is used to get the longest streak. You have to either specify a habit or a timespan.")
@click.option('--habitname', type=str, default="all", help="Specify a habit, if you want to know the longest streak of this specific habit. Default: all")
@click.option('--timespan', type=str, default="all", help="Specify a timespan, if you want to know the longest streak of this specific timespan. Default: all")
def longest_streak(habitname, timespan):
    return_longest_streak(habitname=habitname, timespan=timespan)

@cli.command(name='timespans', help="This command is used to get a list of all specified timespans.")
def timespans():
    return_all_timespans()



if __name__ == '__main__':
    cli()