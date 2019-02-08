import unittest
from os.path import join, dirname, abspath
import sys

root_directory = abspath(join(dirname(__file__), '..', '..', '..', 'src'))

print(root_directory)
sys.path += [root_directory]


from pharmacycounting import test


class TestSortingMethods(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(test, "hi")

    # def test_first_line(self):
        # data_folder = join(dirname(dirname(abspath(__file__))), "output")
        # file_to_open = join(data_folder, "top_drug_cost.txt")
        # with open(file_to_open) as f:
        #     f.readline()
        #     first_line = f.readline()
        # first_drug = "CHLORPROMAZINE,2,3000"
        # self.assertEqual(first_line.strip(), first_drug)

if __name__ == '__main__':

    unittest.main()
