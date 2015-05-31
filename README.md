# Markdown-Parser-Python
A simple Markdown parsing and rendering tool written in Python.


### Parser
```
>>> parse_markdown('This is a paragraph.')
Markdown([Paragraph([Text('This is a paragraph.')])])

>>> parse_markdown('The first paragraph.\\n\\nThe second paragraph.')
Markdown([Paragraph([Text('The first paragraph.')]), Paragraph([Text('The second paragraph.')])])

>>> parse_markdown('Emphasis *is* supported.')
Markdown([Paragraph([Text('Emphasis '), Emphasis('is'), Text(' supported.')])])

>>> parse_markdown('Bold **is** supported.')
Markdown([Paragraph([Text('Bold '), Bold('is'), Text(' supported.')])])

>>> parse_markdown('- a list')
Markdown([List([Paragraph([Text('a list')])])])

>>> parse_markdown('- the first item\\n- the second item')
Markdown([List([Paragraph([Text('the first item')]), Paragraph([Text('the second item')])])])

>>> parse_markdown('- Emphasis *is* supported.')
Markdown([List([Paragraph([Text('Emphasis '), Emphasis('is'), Text(' supported.')])])])

>>> parse_markdown('* the first item\\n* the second item')
Markdown([List([Paragraph([Text('the first item')]), Paragraph([Text('the second item')])])])

>>> parse_markdown('- item1\\n- item2\\n - item2.1\\n - item2.2\\n- item3')
Markdown([List([Paragraph([Text('item1')]), Paragraph([Paragraph([Text('item2')]), List([Paragraph([Text('item2.1')]), Paragraph([Text('item2.2')])])]), Paragraph([Text('item3')])])])

>>> parse_markdown('#######this is header')
Markdown([Paragraph([Header(6,[Text('#this is header')])])])

>>> parse_markdown('#######this is *header* and **header**')
Markdown([Paragraph([Header(6,[Text('#this is '), Emphasis('header'), Text(' and '), Bold('header'), Text('')])])])

>>> parse_markdown('#header1\\n##header2\\n\\nanother paragraph')
Markdown([Paragraph([Header(1,[Text('header1')]), Header(2,[Text('header2')])]), Paragraph([Text('another paragraph')])])

>>> parse_markdown('hello ##this is not *header* and **header**')
Markdown([Paragraph([Text('hello ##this is not '), Emphasis('header'), Text(' and '), Bold('header'), Text('')])])
```


### Usage
```
python render.py test.md
```
