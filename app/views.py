# -*- coding: utf-8 -*-
"""
    Routes for the website
"""
import os.path
import pygments.formatters
from flask import render_template
from flask import Markup
from flask import abort
from flask import safe_join
from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from app import app

# For restructured text
#from docutils.core import publish_partsi

#@app.template_filter('rst')
#def rst_filter(text):
#    return Markup(publish_parts(source=text, writer_name='html')['body'])

@app.template_filter('markdown')
def markdown_filter(text):
    """ Convert markdown to html """
    return Markup(markdown(text, extensions=[CodeHiliteExtension(linenums=True, css_class='highlight'), ExtraExtension()]))

def get_post_dir():
    return os.path.dirname(os.path.abspath(__file__)) + '/content/posts'

def get_post_items():
    items = os.listdir(get_post_dir())
    items.sort(reverse=True)
    return items

def get_posts():
    posts = []
    for item in get_post_items():
        posts.append(item)
    return posts

@app.route('/')
#@app.route('/', methods=['GET', 'POST'])
#@app.route('/index', methods=['GET', 'POST'])
#@app.route('/index/<int:page>', methods=['GET', 'POST'])
def index():
    #post_dir = 'app/content/posts/%s%s'%(path, '.md')
    return render_template('index.html', title='Home')

@app.route('/<path:path>/')
def page(path):
    page = 'app/content/pages/%s%s'%(path, '.md')
    if os.path.isfile(page):
        with open(page, 'r') as f:
            content = f.read()
            return render_template('page.html', page_html=content)
    else:
        abort(404)

@app.route('/blog/')
def blog():
    content = get_posts()
    return render_template('blog.html', page_html=content)

#@app.route('/blog/<int:year>/<int:month>/<slug>')

#@app.route('/blog/<tag>/<slug>/')

#@app.route('/<int:year>/')
#def year_index(year):
#    year_dir = 'app/content/posts/%s'%(year)
#    if os.path.isdir(year_dir):
#        entries = filter(path.isfile, os.listdir(year_dir))
#        return render_template('yearindex.html', page_html=entries)
#    else:
#        abort(404)

@app.route('/feed')
@app.route('/feed.atom')
def feed():
    xml = render_template('atom.xml', **locals())
    return app.response_class(xml, mimetype='application/atom+xml')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
