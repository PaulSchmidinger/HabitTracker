from db import get_db

def td_habit(db):
    cur = db.cursor()
    cur.execute("INSERT INTO Habits (name, create_d, active, timespan) VALUES ('Fencing','2022-09-20 14:13:35','0','1')")
    db.commit()

    cur = db.cursor()
    cur.execute("INSERT INTO Habits (name, create_d, active, timespan) VALUES ('Jogging','2022-09-20 14:13:35','1','1')")
    db.commit()

    cur = db.cursor()
    cur.execute("INSERT INTO Habits (name, create_d, active, timespan) VALUES ('Cycling','2022-09-30 07:19:22','1','1')")
    db.commit()

    cur = db.cursor()
    cur.execute("INSERT INTO Habits (name, create_d, active, timespan) VALUES ('Workout','2022-10-05 11:18:36','1','1')")
    db.commit()

    cur = db.cursor()
    cur.execute("INSERT INTO Habits (name, create_d, active, timespan) VALUES ('Gymnastics','2022-10-10 05:35:46','1','2')")
    db.commit()

    cur = db.cursor()
    cur.execute("INSERT INTO Habits (name, create_d, active, timespan) VALUES ('Hiking','2022-10-17 18:34:22','1','1')")
    db.commit()



    ################

    datetime	habit_id	in_time
2022-09-20 14:14:06	1	1
2022-09-24 18:15:23	2	1
2022-09-26 14:20:45	1	1
2022-10-05 07:23:14	1	0
2022-09-26 17:15:12	2	1
2022-10-02 20:18:43	2	1
2022-10-08 11:18:54	2	1
2022-10-13 18:28:17	2	1
2022-10-17 19:12:57	2	1
2022-09-30 07:22:18	3	1
2022-10-06 11:15:48	3	1
2022-10-14 14:32:36	3	0
2022-10-16 11:22:15	3	1
2022-10-05 11:19:12	4	1
2022-10-11 17:12:15	4	1
2022-10-17 22:10:09	4	1
2022-10-17 18:36:12	6	1
2022-10-10 05:37:36	5	1
2022-10-11 05:40:27	5	1
2022-10-12 06:03:17	5	1
2022-10-13 05:53:55	5	1
2022-10-14 05:38:19	5	1
2022-10-15 05:40:57	5	1
2022-10-16 05:17:05	5	1
2022-10-18 06:02:58	5	0


    #########



td_habit(get_db())