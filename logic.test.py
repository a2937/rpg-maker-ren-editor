import unittest
from logic import transform,restore

class TestTransform(unittest.TestCase):
  def test_empty_string_returns_empty(self):
      self.assertEqual(transform(""),"") 

  def test_returns_autoplay(self):
     self.assertEqual(transform('{"autoplayBgm":true,"autoplayBgs":true}'),"autoplayBgm:true\nautoplayBgs:true")
    
class TestDeTransform(unittest.TestCase):
   def test_empty_returns_empty_json(self):
      self.assertEqual(restore(""),"{}") 

def test_rows_return_autoplay(self):
      self.assertEqual(restore("autoplayBgm:true\nautoplayBgs:true"),'{"autoplayBgm":true,"autoplayBgs":true}') 


if __name__ == '__main__':
    unittest.main()