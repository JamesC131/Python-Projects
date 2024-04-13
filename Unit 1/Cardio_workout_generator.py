import random

miles = random.randint(3, 10)
time = random.randint(15, 30)
time2 = random.randint(20, 30)
workout_type = random.randint(1, 2)
terrain_type = random.randint(1, 2)

if workout_type == 1:
    print("Distance")
    print("Miles: ", miles)
elif workout_type == 1 and terrain_type == 1:
    print("Timed")
    print("Minutes: ", time2)
else:
    print("Timed")
    print("Minutes: ", time)

if terrain_type == 1:
    print("Flat")
else:
    print("Hills")
