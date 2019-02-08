import unittest
from os.path import join, dirname, abspath
import sys

root_directory = abspath(join(dirname(__file__), '..', '..', '..', 'src'))

print(root_directory)
sys.path += [root_directory]


class TestSortingMethods(unittest.TestCase):

    def test_first_line(self):
        data_folder = abspath(join(dirname(__file__), '..', '..', '..', 'output'))
        file_to_open = join(data_folder, "top_drug_cost.txt")
        with open(file_to_open) as f:
            f.readline()
            first_line = f.readline()
        answer_folder = join(dirname(dirname(abspath(__file__))), "test1", "output")
        answer_file_to_open = join(answer_folder, "top_drug_cost.txt")
        with open(answer_file_to_open) as a:
            a.readline()
            answer_first_line = a.readline()
        self.assertEqual(first_line.strip(), answer_first_line.strip())

if __name__ == '__main__':

    unittest.main()
