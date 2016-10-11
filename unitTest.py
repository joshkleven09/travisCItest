import unittest
import HelloWorld as HW

def test_HelloWorldWrong():
    result = HW.printHelloWorld()
    assert result == "Hello World"
    
def test_HelloWorld():
    result = HW.printHelloWorld()
    assert result == "Hello World!"



