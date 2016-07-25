from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re
import os


class ImgPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            m = re.match(r"\!\[(\w*)\]\((.*)\)", line)
            if m:
                basename = os.path.basename(m.group(2))
                new_path = os.path.join('/static/', basename)
                new_line = '![%s](%s)' % (m.group(1), new_path)
                new_lines.append(new_line)
            else:
                new_lines.append(line)

        return new_lines


class ImgStaticLinkExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('static_img', ImgPreprocessor(md), '>reference')
