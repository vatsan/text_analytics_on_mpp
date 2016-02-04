
import unittest
from skip_gram_generator import generate_k_skip_n_gram

class TestSkipgramGenerator(unittest.TestCase):
    def test2skipbigram(self):
        lst = ['insurgents', 'killed', 'in', 'ongoing', 'fighting']
        expected_result = [
                ['insurgents', 'killed'], ['insurgents', 'in'], ['insurgents', 'ongoing'], 
                ['killed', 'in'], ['killed', 'ongoing'], ['killed', 'fighting'], 
                ['in', 'ongoing'], ['in', 'fighting'], ['ongoing', 'fighting']
            ]
        self.assertEqual(generate_k_skip_n_gram(lst, 2, 2), expected_result)

    def test2skiptrigram(self):
        lst = ['insurgents', 'killed', 'in', 'ongoing', 'fighting']
        expected_result = [
            ['insurgents', 'killed', 'in'], 
            ['insurgents', 'killed', 'ongoing'], 
            ['insurgents', 'killed', 'fighting'], 
            ['insurgents', 'in', 'ongoing'], 
            ['insurgents', 'in', 'fighting'], 
            ['insurgents', 'ongoing', 'fighting'], 
            ['killed', 'in', 'ongoing'], 
            ['killed', 'in', 'fighting'], 
            ['killed', 'ongoing', 'fighting'], 
            ['in', 'ongoing', 'fighting']
        ]
        self.assertEqual(generate_k_skip_n_gram(lst, 2, 3), expected_result)        

if(__name__ =='__main__'):
    unittest.main()