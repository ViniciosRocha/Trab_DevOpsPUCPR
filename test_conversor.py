import unittest
from conversor import celsius_para_fahrenheit, fahrenheit_para_celsius

class TestConversor(unittest.TestCase):
    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)
        self.assertEqual(celsius_para_fahrenheit(100), 212)
    
    def test_fahrenheit_para_celsius(self):
        self.assertEqual(fahrenheit_para_celsius(32), 0)
        self.assertEqual(fahrenheit_para_celsius(212), 100)

if __name__ == "__main__":
    print("Rodando testes...")
    unittest.main()
