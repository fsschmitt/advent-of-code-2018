from calendar.day1 import DayOne

advent_calendar = [
    DayOne(),
]

if __name__ == "__main__":
    for day in advent_calendar:
        day.save_christmas()
