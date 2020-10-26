import unittest
from docx_to_latex.docx.parse_docx import ParseDocx

class TestAll(unittest.TestCase):
    def test_all(self):
        pd = ParseDocx("files/test.docx")
        print(pd.parse())


if __name__ == '__main__':
    unittest.main()
