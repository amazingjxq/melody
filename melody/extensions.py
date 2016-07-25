from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re


class ImgPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            m = re.match(r"\!\[\w*\]\((.*)\)", line)
            if m:
                print m.group(1)
            else:
                new_lines.append(line)

        return new_lines


class ImgStaticLinkExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('static_img', ImgPreprocessor(md), '>reference')
