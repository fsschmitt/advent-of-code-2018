from .challenge import DailyChallenge
from .utils.file import read_lines


class DayTwo(DailyChallenge):
    input_list = read_lines('input-2.txt')

    def __init__(self):
        super().__init__("Two")

    def _part1(self):
        sum_two, sum_three = 0, 0
        for box_id in self.input_list:
            matches = {}
            for digit in box_id:
                matches[digit] = matches[digit] + 1 if digit in matches else 1

            if 2 in matches.values():
                sum_two += 1
            if 3 in matches.values():
                sum_three += 1

        return sum_two * sum_three

    def _part2(self):
        for box_id in self.input_list:
            for box_id2 in self.input_list:
                match = [i for i in range(len(box_id)) if box_id[i] != box_id2[i]]
                if len(match) == 1:
                    return box_id[:match[0]] + box_id[match[0]+1:]
        return None


if __name__ == "__main__":
    DayTwo().save_christmas()