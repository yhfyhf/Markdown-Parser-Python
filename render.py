# -*- encoding: utf-8 -*-
from parser import parse_markdown, Markdown, Paragraph, List, Text, Emphasis, Bold, Header
from error import ItemTypeError
import sys


def render(markdown):
    if not isinstance(markdown, Markdown):
        return
    html = ''
    for block in markdown.blocks:
        if isinstance(block, Paragraph):
            html += render_paragraph(block)
        elif isinstance(block, List):
            html += render_list(block)
        else:
            raise ItemTypeError(type(block))
    return html


def render_paragraph(paragraph, in_list=False):
    html = ''
    for item in paragraph.items:
        if isinstance(item, Text):
            html += render_text(item)
        elif isinstance(item, List):
            html += render_list(item, in_list=True)
        elif isinstance(item, Header):
            html += render_header(item)
        elif isinstance(item, Emphasis):
            html += render_emphasis(item)
        elif isinstance(item, Bold):
            html += render_bold(item)
        elif isinstance(item, Paragraph):
            html += render_paragraph(item, in_list=in_list)
        else:
            raise ItemTypeError(type(item))
    return html if in_list else '<p>%s</p>\n' % html


def render_list(l, in_list=False):
    html = ''
    if not in_list:
        for item in l.items:
            html += '\t<li>\n\t\t' + render_paragraph(item, in_list=True) + '\n\t</li>\n'
    else:
        for item in l.items:
            html += '\t\t\t<li>' + render_paragraph(item, in_list=True) + '</li>\n'
    return '\n<ul>\n%s</ul>\n' % html if not in_list else '\n\t\t<ul>\n%s\t\t</ul>' % html


def render_header(header):
    level = header.level
    html = ''
    for item in header.items:
        if isinstance(item, Emphasis):
            emphasis = render_emphasis(item)
            html += emphasis
        if isinstance(item, Bold):
            bold = render_bold(item)
            html += bold
        else:  # item is Text
            html += render_text(item)
    return '\n<h%d>%s</h%d>\n' % (level, html, level)


def render_emphasis(emphasis):
    return '<em>%s</em>' % (emphasis.text)


def render_bold(bold):
    return '<b>%s</b>' % (bold.text)


def render_text(text):
    return text.text


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            string = f.read()
            markdown = parse_markdown(string)
            with open('%s.html' % filename.split('.')[0], 'w') as html_f:
                html_f.write(render(markdown))
    except IndexError:
        print "Please specify the markdown file to be converted."
    except IOError:
        print "File does not exist."
