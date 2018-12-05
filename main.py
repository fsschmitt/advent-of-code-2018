from calendar.day1 import DayOne
from calendar.day2 import DayTwo

advent_calendar = [
    DayOne(),
    DayTwo(),
]

if __name__ == "__main__":
    for day in advent_calendar:
        day.save_christmas()
