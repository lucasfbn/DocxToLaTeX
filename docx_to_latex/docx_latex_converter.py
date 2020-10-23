from pathlib import Path

from docx_to_latex.docx import Docx
from docx_to_latex.latex import LaTex


class DocxToLaTeX:

    def __init__(self, docx_path, tex_template_path, pdf_out_path=None, save_rendered_template=False,
                 convert_newlines=False):
        self.docx_in_path = docx_path
        self.tex_template_path = tex_template_path
        self.pdf_out_path = pdf_out_path

        self._save_rendered_template = save_rendered_template

        self._convert_newlines = convert_newlines
        self.parse_dict = self._load_docx()

    def _load_docx(self):
        return Docx(self.docx_in_path).parse(self._convert_newlines)

    def add_custom_key_val(self, key, val):
        if key in self.parse_dict:
            raise ValueError("You used the same tag twice.")

        self.parse_dict[key] = val

    def convert(self, engine: str = "pdflatex"):
        l = LaTex(self.tex_template_path, self.pdf_out_path)
        l.generate_tex_file(parse_dict=self.parse_dict, save_rendered_tex=self._save_rendered_template)
        l.compile(engine)
