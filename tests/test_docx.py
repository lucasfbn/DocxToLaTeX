from docx_to_latex.docx.docx import Docx

d = Docx("files/test.docx")
print(d.parse())
