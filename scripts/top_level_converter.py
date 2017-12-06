import sys
from nbconvert import HTMLExporter
import nbformat

notebook_file = sys.argv[1]
html_exporter = HTMLExporter()
nb = nbformat.reads(open(notebook_file, 'r').read(), as_version=4)

(body, resources) = html_exporter.from_notebook_node(nb)


read_navbar = open("top_navbar.txt", 'r').read()
read_css = open("top_main_css.txt", 'r').read()

if read_navbar not in body:
    body = body.replace("<body>", "<body>\n" + read_navbar)

if read_css not in body:
    body = body.replace("</title>", "</title>\n" + read_css)

html_file = notebook_file.replace(".ipynb", ".html")
html_file_writer = open(html_file, 'w')
html_file_writer.write(body)
html_file_writer.close()
