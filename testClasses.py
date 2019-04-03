import classes
import unittest
import io
import sys

class TestClass(unittest.TestCase):
    p1 = classes.Person('Shubhang','Rewa',['Weed-Dealer',])

    def test_fullobj(self):
        output_text = io.StringIO()
        sys.stdout = output_text
        self.p1.show()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_text.getvalue(),'My name is Shubhang and my current city is Rewa\n')

    p3 = classes.Person('Vinay')

    def test_no_work(self):
        try:
            self.p3.work
        except AttributeError:
            pass

    def tearDown(self):
        del self

    def test_partialobj(self):
        output_text = io.StringIO()
        sys.stdout = output_text
        self.p3.show()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_text.getvalue(), 'My name is Vinay and my current city is Roorkee\n')

    
if __name__ == '__main__':
    unittest.main()