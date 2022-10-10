import cl_ht
import db

habit = cl_ht.habits("test", "Day")
print(habit.name)
print(habit.timespan)
print(habit.created_t)
print(habit.active)
print("###############")

habit.deactivate_habit()
print(habit.active)