#PS

import click
from cl_ht import habits, completion
from analyse import return_all_timespans, return_habits, return_longest_streak

print("Welcome to the habit tracker backend.")

@click.group()
def cli():
    pass    

@cli.command(name='create_habit')
@click.option('--name', type=str)
@click.option('--timespan', type=str)
def create_habit(name, timespan):
    habits(name=name, timespan=timespan)

@cli.command(name='dea_habit')
@click.option('--name', type=str)
def dea_habit(name):
    habits.deactivate_habit(name)

@cli.command(name='check')
@click.option('--name', type=str)
def check(name):
    compl = completion()
    compl.check_habit(name)

@cli.command(name='habits')
@click.option('--all', is_flag=True)
@click.option('--timespan', type=str, default="all")
def habits(all, timespan):
    if all:
        return_habits(all=1, timespan=timespan)
    else:
        return_habits(all=0, timespan=timespan)

@cli.command(name='longest_streak')
@click.option('--habitname', type=str, default="all")
@click.option('--timespan', type=str, default="all")
def longest_streak(habitname, timespan):
    return_longest_streak(habitname=habitname, timespan=timespan)

@cli.command(name='timespans')
def timespans():
    return_all_timespans()



if __name__ == '__main__':
    cli()