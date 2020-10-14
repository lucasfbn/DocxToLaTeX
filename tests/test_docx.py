from docx_to_latex.docx import Docx

d = Docx("files/test.docx")
print(d.parse())
