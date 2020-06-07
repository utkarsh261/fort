import os
import sys
import unittest
from fort import imgtools

class TestMe(unittest.TestCase):
   def test_stuff(self):
       path = os.path.join(sys.path[0], 'test/img.jpg')
       obj = imgtools.ImgTools()
       hsh = obj.get_dhash(path)
       assert hsh=="e0f0746e6ce4e42c"


if __name__ == '__main__':
    unittest.main()