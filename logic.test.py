import unittest
from logic import transform

class TestTransform(unittest.TestCase):
  def test_empty_string_returns_empty(self):
      self.assertEqual(transform(""),"") 

  def test_returns_autoplay(self):
     self.assertEqual(transform('{"autoplayBgm":true,"autoplayBgs":true}'),"autoplayBgm:true\nautoplayBgs:true")
    
  

if __name__ == '__main__':
    unittest.main()