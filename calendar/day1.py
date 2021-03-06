from itertools import cycle
from .challenge import DailyChallenge
from .utils.file import read_lines


class DayOne(DailyChallenge):
    input_list = list(map(int, read_lines('input-1.txt')))

    def __init__(self):
        super().__init__("One")

    def _part1(self):
        return sum(self.input_list)

    def _part2(self):
        all_freq = set()
        current_freq = 0
        for change in cycle(self.input_list):
            all_freq.add(current_freq)
            current_freq += change
            if current_freq in all_freq:
                return current_freq
        return None


if __name__ == "__main__":
    DayOne().save_christmas()
