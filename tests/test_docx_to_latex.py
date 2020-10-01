import unittest
import os
from src.docx_to_latex import DocxToLaTeX

class TestDocxToLatex(unittest.TestCase):
    def test_convert(self):

        dl = DocxToLaTeX(docx_path="test.docx", tex_template_path="test.tex", save_rendered_template=True)
        dl.convert()

    def test_add_custom_key(self):
        dl = DocxToLaTeX(docx_path="test.docx", tex_template_path="test_with_custom.tex", save_rendered_template=True)
        dl.add_custom_key_val("test", "worked")
        dl.convert()



if __name__ == '__main__':
    unittest.main()
