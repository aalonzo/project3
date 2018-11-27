import unittest
from professor import *

class test_Main(unittest.TestCase):

    def test_1_valid_input_with_result(self): # search with valid input and returned results
        prof = Professor("mullins")

        self.assertEqual(prof.rating, "5.0")
        self.assertEqual(prof.difficulty, "4.0")

    def test_2_valid_input_with_no_result(self): # search with valid input, but no results
        prof = Professor("wafflecone")

        self.assertIsNone(prof.rating)
        self.assertIsNone(prof.difficulty)

    def test_3_invalid_input(self): # search with invalid input (non-alphanumeric input)
        prof = Professor("/////")

        self.assertIsNone(prof.rating)
        self.assertIsNone(prof.difficulty)
        
    def test_4_find_professor_single_result(self):
        result=find_professor("Richard Fitzpatrick"):
        
        self.assertEqual(result, ["http://www.ratemyprofessors.com/ShowRatings.jsp?tid=1035306"])
        
    def test_5_find_professor_multiple_result(self):
        result=find_professor("Wolesensky"):
        
        self.assertEqual(result, ["http://www.ratemyprofessors.com/ShowRatings.jsp?tid=1865488","http://www.ratemyprofessors.com/AddRating.jsp?tid=2152246"])
        
    def test_6_find_professor_no_result(self):
        result=find_professor("Wolensensky"):
        
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
