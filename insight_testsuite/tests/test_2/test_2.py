import unittest
from os.path import join, dirname, abspath
import sys

root_directory = abspath(join(dirname(__file__), '..', '..', '..', 'src'))

print(root_directory)
sys.path += [root_directory]


class TestSortingMethods(unittest.TestCase):

    data_folder = abspath(join(dirname(__file__), '..', '..', '..', 'output'))
    file_to_open = join(data_folder, "top_cost_drug.txt")

    answer_folder = join(dirname(dirname(abspath(__file__))), "test_2", "output")
    answer_file_to_open = join(answer_folder, "top_cost_drug.txt")

    def test_first_line(self):

        with open(self.file_to_open) as f:
            f.readline()
            first_line = f.readline()
        with open(self.answer_file_to_open) as a:
            a.readline()
            answer_first_line = a.readline()
        self.assertEqual(first_line.strip(), answer_first_line.strip())

if __name__ == '__main__':

    unittest.main()
