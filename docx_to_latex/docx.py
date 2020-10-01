import re
import docx2txt


class Docx:

    start_tag = "<"
    end_tag = ">"

    def __init__(self, path):
        self.doc = docx2txt.process(path)
        self._validate()

    def _validate(self):
        # Validate we have all matching opening and closing brackets:
        opening_brackets = re.findall(r'<[^/]*>', self.doc)
        closing_brackets = re.findall(r'</.*>', self.doc)

        assert len(opening_brackets) == len(
            closing_brackets), f"Missing opening or closing brackets. Opening brackets: {len(opening_brackets)}," \
                               f" Closing brackets: {len(closing_brackets)}"

    def parse(self):

        parse_dict = {}

        for match in re.finditer(r'<(.*)>(.|\n)*?</\1>', self.doc):

            text = match.group()

            # Find entry key like {test} but NOT {\test}
            key = re.search(r'<[^/].*>', text).group()
            # Removes "{" and "}"
            key = re.sub(r'([<>])', "", key)
            # Get text between tags

            if key in parse_dict:
                raise ValueError("You used the same tag twice.")

            parse_dict[key] = re.sub(r'<.*>', "", text).replace("\n", "").replace('\r', '').strip()

        return parse_dict

