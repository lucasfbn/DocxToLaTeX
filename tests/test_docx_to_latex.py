import unittest
import os
from docx_to_latex.docx_latex_converter import DocxToLaTeX


class TestDocxToLatex(unittest.TestCase):
    def test_convert(self):
        dl = DocxToLaTeX(docx_path="files/test.docx", tex_template_path="files/test.tex", save_rendered_template=True,
                         pdf_out_path="files/test.pdf")
        dl.convert()

    def test_add_custom_key(self):
        dl = DocxToLaTeX(docx_path="files/test.docx", tex_template_path="files/test_with_custom.tex",
                         save_rendered_template=True, pdf_out_path="files/test.pdf")
        dl.add_custom_key_val("test", "worked")
        dl.convert()


if __name__ == '__main__':
    unittest.main()
