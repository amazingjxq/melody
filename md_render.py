#!/usr/bin/env python
"""markdown2html

Usage:
    markdown2html.py <md> <html_path>
"""
from docopt import docopt
import markdown
from jinja2 import Environment, PackageLoader
import os
import shutil
from pygments.styles import get_style_by_name
from pygments.styles import get_all_styles
from pygments.formatters import HtmlFormatter


class MDRenderException(Exception):
    pass


class MDRender:
    def __init__(self, markdown_file):
        "docstring"
        self.markdown_file = markdown_file
        self.extensions = [
            "markdown.extensions.codehilite",
            "markdown.extensions.tables",
            "markdown.extensions.fenced_code"]
        self.env = Environment(loader=PackageLoader('md_render', 'templates'))
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



def render(md_content):
    html = markdown.markdown(md_content,
                             extensions=["markdown.extensions.codehilite",
                                         "markdown.extensions.tables",
                                         "markdown.extensions.fenced_code"])

    env = Environment(loader=PackageLoader('md_render', 'templates'))
    tpl = env.get_template('github.html')
    return tpl.render(md_html=html)


def create_dir(html_path):
    if not os.path.exists(html_path):
        os.makedirs(html_path)

    css_path = os.path.join(html_path, "css")
    if not os.path.exists(css_path):
        os.makedirs(css_path)


def copy_css(html_path):
    package_path = os.path.dirname(__file__)
    src_css_path = os.path.join(package_path, "css")
    dst_css_path = os.path.join(html_path, "css")

    shutil.copy(os.path.join(src_css_path, "code.css"), dst_css_path)
    shutil.copy(os.path.join(src_css_path, "github-markdown.css"), dst_css_path)


def write_html(md_path, html_path, html_content):
    path, md_path_base = os.path.split(md_path)
    md_path_base_file, md_path_base_extension = os.path.splitext(md_path_base)

    html_file = os.path.join(html_path, md_path_base_file + ".html")
    html_fd = open(html_file, "w")
    html_fd.write(html_content.encode("utf-8"))
    html_fd.close()


def process(md_path, html_path):
    # md_fd = open(md_path, 'r')
    # md_content = md_fd.read().decode("utf-8")

    # html_content = render(md_content)

    # create_dir(html_path)

    # write_html(md_path, html_path, html_content)

    # copy_css(html_path)
    render = MDRender(md_path)
    print render.render('github', 'tango')


def main():
    args = docopt(__doc__, version='0.1')
    process(args['<md>'], args['<html_path>'])

if __name__ == '__main__':
    main()
