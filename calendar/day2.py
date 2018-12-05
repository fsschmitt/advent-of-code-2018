from .challenge import DailyChallenge
from .utils.file import read_lines


class DayTwo(DailyChallenge):
    input_list = read_lines('input-2.txt')

    def __init__(self):
        super().__init__("Two")

    def _part1(self):
        sum_two, sum_three = [0, 0]
        for box_id in self.input_list:
            # [one-time, two-times, three-times, more]
            list_matches = [set(), set(), set(), set()]
            for digit in box_id:
                for exact_times in list_matches:
                    if not digit in exact_times:
                        exact_times.add(digit)
                        break
            two_matches = list_matches[1] - list_matches[2] - list_matches[3]
            three_matches = list_matches[2] - list_matches[3]
            sum_two += 1 if two_matches else 0
            sum_three += 1 if three_matches else 0
        return sum_two * sum_three

    def _part2(self):
        final_box_id = ""
        for box_id in self.input_list:
            found_match = False
            for box_id2 in self.input_list:
                match = [i for i in range(len(box_id)) if box_id[i] != box_id2[i]]
                if len(match) == 1:
                    found_match = True
                    break
            if found_match:
                final_box_id = box_id[:match[0]] + box_id[match[0]+1:]
                break
        return final_box_id


if __name__ == "__main__":
    DayTwo().save_christmas()