import sys
import markdown

from settings import MARKDOWN_CSS,MARKDOWN_EXT,PYGMENTS_CSS

def markdown_processor(options):
    return markdown.Markdown(**options)

def read_input(input_file,encoding=None):
    encoding = encoding or 'utf-8'
    text = ''
    if input_file == '-':
        text = sys.stdin.read()
        if not isinstance(text,str):
            text = text.decode(encoding)
    elif input_file:
        if isinstance(input_file,str):
            if not os.path.exists(input_file):
                with open(input_file.mode='w'):
                    pass
    input_file = codecs.open(input_file, mode="rb", encoding=encoding)
        else:
            input_file = codecs.getreader(encoding)(input_file)
        text = input_file.read()
        input_file.close()
    text = text.lstrip('\ufeff')
    return text

class MarkdownDocument(object):
    def __init__(self, mdtext='', infile=None, outfile=None, md=None, markdown_css=MARKDOWN_CSS, pygments_css=PYGMENTS_CSS ):
        self.input_file = infile
        self.output_file = outfile
        initial_markdown = mdtext and mdtext or read_input(self.input_file)
        self.inline_css = ''

        if markdown_css:
            with open(markdown_css) as markdown_css_file:
                self.inline_css += markdown_css_file.read()

        if pygments_css:
            with open(pygments_css) as pygments_css_file:
                self.inline_css += pygments_css_file.read()

        if not md:
            self.md = markdown.Markdown(extensions=MARKDOWN_EXT)
        else:
            self.md = md

        self.text = initial_markdown
        self.form_data = {} # used by clients to handle custom form actions

    def getHtml(self):
        return self.md.convert(self.text)

    def getHtmlPage(self):
        return """<!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <style type="text/css">
        %s
        </style>
        </head>
        <body>
        <div class="markdown-body">
        %s
        </div>
        </body>
        </html>
        """ % (self.inline_css, self.getHtml())
