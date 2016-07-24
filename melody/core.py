#!/usr/bin/env python
import markdown
from jinja2 import Environment, PackageLoader
import os
import shutil
from pygments.styles import get_style_by_name
from pygments.styles import get_all_styles
from pygments.formatters import HtmlFormatter


class MelodyRenderException(Exception):
    pass


class MelodyRender:
    def __init__(self, markdown_file):
        "docstring"
        self.markdown_file = markdown_file
        self.extensions = [
            "markdown.extensions.codehilite",
            "markdown.extensions.tables",
            "markdown.extensions.fenced_code"]
        self.env = Environment(loader=PackageLoader('melody', 'templates'))
        self.templates = {
            'github': 'github.html',
        }
        self.styles = list(get_all_styles())
        self.rendered_html = ''

    def render(self, template, style):
        if template not in self.templates:
            raise MDRenderException('Invalid template')

        if style not in self.styles:
            raise MDRenderException('Invalid style')

        with open(self.markdown_file) as md_fd:
            md_content = md_fd.read().decode("utf-8")
            html_content = markdown.markdown(md_content,
                                             extensions=self.extensions)
            tpl = self.env.get_template(self.templates[template])

            code_css = HtmlFormatter(style=style).get_style_defs()

            self.rendered_html = tpl.render(md_html=html_content,
                                            code_css=code_css).encode("utf-8")
            return self.rendered_html

    def export(self):
        pass

def write_html(md_path, html_path, html_content):
    path, md_path_base = os.path.split(md_path)
    md_path_base_file, md_path_base_extension = os.path.splitext(md_path_base)

    html_file = os.path.join(html_path, md_path_base_file + ".html")
    html_fd = open(html_file, "w")
    html_fd.write(html_content.encode("utf-8"))
    html_fd.close()

def joke():
    return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            u'Beiherhund das Oder die Flipperwaldt gersput.')
