import re
from functools import reduce
from .challenge import DailyChallenge
from .utils.file import read_lines


class DayThree(DailyChallenge):
    input_list = read_lines('input-3.txt')
    matrix = None

    def __init__(self):
        super().__init__("Three")

    def _fabric_builder(self):
        h, w = [1000, 1000]
        matrix = [[0 for x in range(w)] for y in range(h)]
        for entry in self.input_list:
            _, left, top, width, height = map(int, re.findall(r'\d+', entry))
            for x in range(width):
                for y in range(height):
                    matrix[left + x][top + y] += 1
        return matrix

    def _is_fabric_unique(self, matrix, left, top, width, height):
        for x in range(width):
            for y in range(height):
                if matrix[left + x][top + y] > 1:
                    return False
            if x == width - 1:
                return True

    def _part1(self):
        inches = 0
        self.matrix = self._fabric_builder()
        for row in self.matrix:
            inches += sum(i > 1 for i in row)
        return inches

    def _part2(self):
        # avoid rebuilding the matrix
        matrix = self.matrix if self.matrix else self._fabric_builder()
        
        for entry in self.input_list:
            id, left, top, width, height = map(int, re.findall(r'\d+', entry))
            if self._is_fabric_unique(matrix, left, top, width, height):
                return id
        return None


if __name__ == "__main__":
    DayThree().save_christmas()
