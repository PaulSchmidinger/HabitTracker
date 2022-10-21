#PS
from db import get_db, get_habits, get_timespans, get_streak_data

def return_habits(all:int = 1, timespan:str="all"):
    """Returns a list of all or all active habits. When a periodicity is specified, it will only return the habits with the this periodicity."""
    li_habits = get_habits(get_db(), all=all, timespan=timespan)
    
    if len(li_habits) == 0: print("There are no such habits!")

    for row in li_habits:
        print("Habitname: "+row[0])
        print("Time of creation: "+row[1])
        print("Periodicity: "+str(row[2]).capitalize())
        if all == 1:
            if row[3] == 1:
                print("Active: Yes")
            else:
                print("Active: No")

def return_longest_streak(habitname:str = "all", timespan:str = "all"):
    """Return the longest run streak of all defined habits with the same periodicity or of a given habit. You have to specify either or."""
    df_streak_data = get_streak_data(get_db(),habitname=habitname, timespan=timespan)
    if df_streak_data.empty:
        print('There is no such data. You have to specify either a timespan or a habit. Maybe you have tried to define a deactivated habit. If you specify a habit, you can only check for active habits.')
        return None

    #by habitname
    if timespan == "all" and habitname != "all":
        li_intime = df_streak_data.in_time.to_list()
        str_intime = "".join(str(e) for e in li_intime)
        li_intime = str_intime.split("0")
        li_maxl = []
        for e in li_intime:
            l = len(e)
            li_maxl.append(l)

        if max(li_maxl) == 0:
            print("Your longest run streak for '"+habitname+"' is: "+str(max(li_maxl))+" Periods.")
        else:
            print("Your longest run streak for '"+habitname+"' is: "+str(max(li_maxl))+" Periods. Congratulations!!")


    #by timespan
    elif timespan != "all" and habitname == "all":
        li_unique_habits = df_streak_data.Habitname.unique().tolist()

        li_habit_df = []
        li_maxl = []

        for habit in li_unique_habits:
            df = df_streak_data[df_streak_data['Habitname'] == habit]
            li_habit_df.append(df)

        for df in li_habit_df:
            li_intime = df.in_time.to_list()
            str_intime = "".join(str(e) for e in li_intime)
            li_intime = str_intime.split("0")
            for e in li_intime:
                    l = len(e)
                    li_maxl.append(l)

        if max(li_maxl) == 0:
            print("Your longest run streak for the timespan '"+timespan+"' is: "+str(max(li_maxl))+" Periods.")
        else:
            print("Your longest run streak for the timespan '"+timespan+"' is: "+str(max(li_maxl))+" Periods. Congratulations!!")


def return_all_timespans():
    """Returns all timespans in the database."""
    li_timespans = get_timespans(get_db())

    for row in li_timespans:
        print("Name: "+row[0].capitalize())
        print("Duration: "+str(row[1])+" Days")
