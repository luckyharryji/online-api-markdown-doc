settings = {
    'debug': False,
    'cookie_secret':"cptbtptp"
}

DATABASE_OPTIONS = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'passwd':'19930801',
    'database':'sccs',
    'charset':'utf8',
}

PROJECT_NAME = "MARKDOWN_EDIT"

MARKDOWN_EXT = ('codehilite', 'extra', 'strikethrough')
MARKDOWN_CSS = join(scriptdir, 'styles/markdown.css')
PYGMENTS_CSS = join(scriptdir, 'styles/pygments.css')
