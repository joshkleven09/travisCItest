import unittest
import HelloWorld as HW

def test_HelloWorld():
    result = HW.printHelloWorld()
    assert result == "Hello World!"

