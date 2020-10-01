import os
from pathlib import Path
from subprocess import Popen
import tempfile
import shutil
import re

import jinja2


class LaTex:

    # def __init__(self, tex_template_path, path_pdf_out=None):
    #     self.tex_template_path = None
    #     self.tex_template_path_dir = None
    #     self.path_pdf_out = None
    #
    #     self._handle_dirs(tex_template_path)
    #
    #     self._jinja2_env = self._load_jinja2_env()

    def __init__(self, tex_template_path, path_pdf_out=None):
        self.tex_template_path = None
        self.tex_template_path_dir = None
        self.path_pdf_out = path_pdf_out

        self._handle_dirs(tex_template_path)

        self._jinja2_env = self._load_jinja2_env()
        self.rendered_tex = None

    def _handle_dirs(self, tex_template_path):
        self.tex_template_path = Path(tex_template_path)

        # Get parent dir of input file
        self.tex_template_path_dir = self.tex_template_path.parent.absolute()

        # If no custom pdf out path is given, save the output pdf under the same name and dir as the input docx
        if self.path_pdf_out is None:
            temp = str(self.tex_template_path)
            temp = temp.split(".")[0]
            temp += ".pdf"

            self.path_pdf_out = Path(temp)

    def _load_jinja2_env(self):
        return jinja2.Environment(
            block_start_string='\BLOCK{',
            block_end_string='}',
            variable_start_string='\VAR{',
            variable_end_string='}',
            comment_start_string='\#{',
            comment_end_string='}',
            line_statement_prefix='%%',
            line_comment_prefix='%#',
            trim_blocks=True,
            autoescape=False,
            loader=jinja2.FileSystemLoader(self.tex_template_path_dir))

    def generate_tex_file(self, parse_dict, save_rendered_tex=False):

        tex_template_filename = re.findall(r'\\(\w*)\.', str(self.tex_template_path))[0]
        template = self._jinja2_env.get_template(tex_template_filename)
        self.rendered_tex = template.render(p=parse_dict)

        if save_rendered_tex:
            print(self.tex_template_path_dir / "rendered.tex")
            with open(self.tex_template_path_dir / "rendered.tex", "w+", encoding="utf-8") as f:
                f.write(self.rendered_tex)

    def compile(self):

        # Create a temp dir and write the rendered tex to a temp file
        tmp_dir = tempfile.mkdtemp()
        in_tmp_path = os.path.join(tmp_dir, 'rendered.tex')
        with open(in_tmp_path, 'w+', encoding="utf-8") as outfile:
            outfile.write(self.rendered_tex)

        # Change dir to where the tex template resides in to make LaTeX use dependencies in the same folder (if any)
        os.chdir(self.tex_template_path_dir)

        # Compile
        out_tmp_path = os.path.join(tmp_dir, 'out.pdf')
        p = Popen(['pdflatex', in_tmp_path, '-job-name', 'out', '-output-directory', tmp_dir])
        p.communicate()

        # Copy out.pdf to the specified location and delete the temp dir
        shutil.copy(out_tmp_path, self.path_pdf_out)
        shutil.rmtree(tmp_dir)
