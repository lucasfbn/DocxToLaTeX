from docx import Document


class ParseDocx:

    def __init__(self, path):
        self.doc = Document(path)

    def parse(self):
        text = []

        for para in self.doc.paragraphs:

            para_text = []

            for word in para.runs:
                if word.italic:
                    para_text.append("\\textit{" + word.text + "}")
                elif word.bold:
                    para_text.append("\\textbf{" + word.text + "}")
                else:
                    para_text.append(word.text)

            text.append("".join(para_text))

        return "\n".join(text)
