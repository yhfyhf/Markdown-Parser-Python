# -*- encoding: utf-8 -*-
from parser import parse_markdown, Markdown, Paragraph, List, Text, Emphasis, Bold, Header
from error import ItemTypeError


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
            html += render_list(item)
        elif isinstance(item, Header):
            html += render_header(item)
        elif isinstance(item, Emphasis):
            html += render_emphasis(item)
        elif isinstance(item, Bold):
            html += render_bold(item)
        elif isinstance(item, Paragraph):
            html += render_paragraph(item, in_list)
        else:
            raise ItemTypeError(type(item))
    return html if in_list else '<p>\n\t%s\n</p>\n' % html


def render_list(l):
    html = ''
    for item in l.items:
        html += '\t<li>' + render_paragraph(item, True) + '</li>\n'
    return '\n\t<ul>\n%s</ul>\n' % html


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
    return '<h%d>%s</h%d>\n' % (level, html, level)


def render_emphasis(emphasis):
    return '<em>%s</em>' % (emphasis.text)


def render_bold(bold):
    return '<b>%s</b>' % (bold.text)


def render_text(text):
    return text.text


if __name__ == '__main__':
    with open('test.md', 'r') as f:
        string = f.read()
        markdown = parse_markdown(string)
        with open('index.html', 'w') as html_f:
            html_f.write(render(markdown))
        print render(markdown)
