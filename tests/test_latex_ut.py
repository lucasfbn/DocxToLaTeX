import unittest

from src.latex import LaTex
from pathlib import Path
import os

# class TestDirs(unittest.TestCase):
#
#     def test_relative_input_dir(self):
#         l = LaTex("test.docx")
#         self.assertEqual(l.tex_template_path_dir, Path("D:/OneDrive/Backup/Projects/WordToLatex/tests"))
#
#     def test_absolute_input_dir(self):
#         l = LaTex("D:/OneDrive/Backup/Projects/WordToLatex/tests/test.docx")
#         self.assertEqual(l.tex_template_path_dir, Path("D:/OneDrive/Backup/Projects/WordToLatex/tests"))
#
#     def test_path_pdf_out_none(self):
#         l = LaTex("D:/OneDrive/Backup/Projects/WordToLatex/tests/test.docx")
#         self.assertEqual(l.path_pdf_out, Path("D:/OneDrive/Backup/Projects/WordToLatex/tests/test.pdf"))

class TestDirs(unittest.TestCase):

    def test_relative_input_dir(self):
        l = LaTex("test.tex")
        self.assertEqual(l.tex_template_path_dir, Path("D:/OneDrive/Backup/Projects/WordToLatex/tests"))

    def test_absolute_input_dir(self):
        l = LaTex("D:/OneDrive/Backup/Projects/WordToLatex/tests/test.tex")
        self.assertEqual(l.tex_template_path_dir, Path("D:/OneDrive/Backup/Projects/WordToLatex/tests"))

    def test_path_pdf_out_none(self):
        l = LaTex("D:/OneDrive/Backup/Projects/WordToLatex/tests/test.tex")
        self.assertEqual(l.path_pdf_out, Path("D:/OneDrive/Backup/Projects/WordToLatex/tests/test.pdf"))

class TestGenerateTexFile(unittest.TestCase):

    def test_generate_tex_file(self):
        l = LaTex("test.tex")
        parse_dict = {"one": "testcase one", "second": "testcase two"}
        l.generate_tex_file(parse_dict, save_rendered_tex=True)
        assert os.path.exists(l.tex_template_path_dir / "rendered.tex") is True

        os.remove(l.tex_template_path_dir / "rendered.tex")

class TestCompileTex(unittest.TestCase):

    def test_compile_tex(self):
        l = LaTex("test.tex")
        parse_dict = {"one": "testcase one", "second": "testcase two"}
        l.generate_tex_file(parse_dict, save_rendered_tex=False)
        l.compile()
        assert os.path.exists(l.tex_template_path_dir / "test.pdf") is True

        os.remove(l.tex_template_path_dir / "test.pdf")


if __name__ == '__main__':
    unittest.main()
