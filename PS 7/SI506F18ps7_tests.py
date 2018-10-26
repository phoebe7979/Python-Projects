# -*- coding: utf-8 -*-
import unittest
from SI506F18_ps7 import *

class Problem1(unittest.TestCase):
    def test_python_diction(self):
        with open("python_diction_saved.json") as jsonfile:
            self.assertTrue(jsonfile is not None, "testing that file exists")
            res = json.loads(jsonfile.read())
            self.assertTrue(len(res["items"])>0,"Testing that file has good content")
            jsonfile.close()

class Problem2(unittest.TestCase):
    def test_names_file(self):
        with open("names_zips_ages.csv") as csvfile:
            self.assertTrue(csvfile is not None,"testing that file exists")
            cont = csvfile.read()
            self.assertTrue("NAME" in cont.split("\n")[0])
            self.assertTrue("Brock" in cont)
            csvfile.close()

class Problem3(unittest.TestCase):
    def test_common_word(self):
        self.assertEqual(common_word, "common", "testing value of common_word")

class Problem4(unittest.TestCase):
    def test_function_file(self):
        self.assertEqual(common_file_word("sample_text.txt"),"common")
    def test_function_again(self):
        f = open("testfile.txt","w")
        f.write("hello hello hello hi there 506 hi again hello hello hello\n")
        f.close()
        self.assertEqual(common_file_word("testfile.txt"),"hello","testing function run on a new and separate file")


if __name__ == "__main__":
    unittest.main(verbosity=2)
