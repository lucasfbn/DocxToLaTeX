from docx_to_latex.docx import Docx

d = Docx("test.docx")
print(d.parse())
