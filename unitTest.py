import unittest
from HelloWorld import HelloWorldClass

class TestForTravisCI(unittest.TestCase):
    def test_HelloWorld(self):
        hello = HelloWorldClass()
        result = hello.printHelloWorld()
        self.assertEqual("Hello World", result)

if __name__ == '__main__':
    unittest.main()
