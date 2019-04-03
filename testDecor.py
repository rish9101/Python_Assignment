import io
import sys
import func
import credentials
import unittest


class TestClass(unittest.TestCase):

    def test_userWhichexists(self):
        username = "shaddygarg"
        output_text = io.StringIO()
        sys.stdout = output_text
        func.foo(username)
        sys.stdout = sys.__stdout__
        self.assertEqual(output_text.getvalue(), 'Hey There, shaddygarg .Do you want an avengers\' spoiler??\n')
        
    def test_userwhichdoesntexist(self):
        username = "Rishi"
        output_text = io.StringIO()
        sys.stdout = output_text
        func.foo(username)
        sys.stdout = sys.__stdout__
        self.assertEqual(output_text.getvalue(), "I'm Sorry Rishi\n")
    
if __name__=='__main__':
    unittest.main()
