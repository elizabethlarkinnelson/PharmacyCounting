import unittest
from os.path import join, dirname, abspath


class TestSortingMethods(unittest.TestCase):

    def test_first_line(self):
        
        # data_folder = join(dirname(dirname(abspath(__file__))), "output")
        # file_to_open = join(data_folder, "top_drug_cost.txt")
        # with open(file_to_open) as f:
        #     f.readline()
        #     first_line = f.readline()
        # first_drug = "CHLORPROMAZINE,2,3000"
        # self.assertEqual(first_line.strip(), first_drug)

if __name__ == '__main__':

    unittest.main()
