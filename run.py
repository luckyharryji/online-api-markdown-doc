import logging

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.options import define,options,parse_command_line
from markdown_edit.settings import settings,PROJECT_NAME

define("port", default=8000, help="run on the given port", type=int)
define("create_tables",help="create tables")
define("file",help = "edit this file")


def make_app():
    return Application(**settings)

def main():
    parse_command_line()
    logging.info("Application listen on port %s" % options.port)
    if options.file:
        logging.info("Begin edit %s" % options.file)
    app=make_app()
    app.listen(options.port)
    IOLoop.current().start()

if __name__=='__main__':
    main()
