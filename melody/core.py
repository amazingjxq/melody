#!/usr/bin/env python
import markdown
from jinja2 import Environment, PackageLoader
import os
import shutil
from pygments.styles import get_style_by_name
from pygments.styles import get_all_styles
from pygments.formatters import HtmlFormatter
from melody.extensions import ImgStaticLinkExtension


class MelodyRenderException(Exception):
    pass


class MelodyRender:
    def __init__(self, markdown_file):
        "docstring"
        self.markdown_file = markdown_file
        self.extensions = [
            "markdown.extensions.codehilite",
            "markdown.extensions.tables",
            "markdown.extensions.fenced_code",
            ImgStaticLinkExtension(),
        ]
        self.env = Environment(loader=PackageLoader('melody', 'templates'))
        self.templates = {
            'github': 'github.html',
            'wechat': 'wechat.html',
        }
        self.styles = list(get_all_styles())
        self.rendered_html = ''

    def render(self, template='github', style='tango'):
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

    def export(self, html_file):
        html_fd = open(html_file, "w")
        html_fd.write(html_content.encode("utf-8"))
        html_fd.close()


def joke():
    return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            u'Beiherhund das Oder die Flipperwaldt gersput.')
