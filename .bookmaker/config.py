

import os.path
import ConfigParser as cf



###
# This file and other meta files are per content not for the bookmmaker
# however we need to have a route to the meta dir so all parts of bookmaker
# can  see the templates etc

### where are we - this is in cookbook/meta, but I want just cookbook
working_dir =os.path.dirname(os.path.abspath(__file__))
FULLROOTPATH = os.path.dirname(working_dir)

### location of templates
TEMPLATE_DIR = os.path.join(working_dir, "tmpls")
### setting up the chapter and config locations
configdocs = """
I want config variables to tell me where we are on disk
 the requirement is that there is a structure as below::

     cookbook/  <-- user defined top level holding all the rst.
       .bookmaker/  <-- required name
         config.py  <-- this file
         __init__.py <-- needed to import config !!! try using configparser one day
  
""" 
 
chapters_dir = os.path.split(os.path.split(__file__)[0])[0]
SOURCE_RST_ROOT = chapters_dir
IMG_DIR = os.path.join(chapters_dir, "img")
CSS_DIR = os.path.join(chapters_dir, "css")




### CONSTANTS 
## the root that will be added to all (relative?) urls
HTMLROOT = "/book"
css_theme = 'theme_sphinx.css' #'cookbook.css'  #set this to the stylesheet we want to use.



BINARYPATH = os.path.abspath('./')

HTML_DIR = '/tmp/bookbuild'
HTML_DEPLOY_DIR = "/usr/local/www/nginx/book"


### valid exts for files that are raw test
valid_exts = ['.chp',]


## new config

HTML_BUILD_DIR = os.path.join(HTML_DIR, 'html')
PATH_FROM_DOCROOT = HTMLROOT
DEPLOY_HTML_ROOT = HTML_DEPLOY_DIR

### setting front page
frontpage_list_articles =  ["Attitude/whatswrongwithagile.chp",
    "Attitude/ibmadverts.chp", "SoHoFromScratch/time.chp",
    "Attitude/business_case.chp"]



logfilepath = os.path.join(FULLROOTPATH, 'log.log')

###
incl_file_name = '.ppp_include'
IGNORE_EXCLUDE = False         # if true put every file into site.  This is set with argument flag to make simple for me to review site.

latex_dir  = 'simpleITmanager_latex'

####### No longer used - using html_parts
#cmdpath = '/usr/home/pbrian/downloads/docutils-0.5/tools/rst2html.py'
#cmdpath = 'rst2html.py'
#
#rst_options = ['--stylesheet-path=css/thebook.css', 
#               '--initial-header-level=3',
#               '--link-stylesheet']
rst2html_overrides = { 'input_encoding': "unicode",
                       'initial_header_level': 2,
                       'styleheet-path':'css/thebook.css',
                       'link-stylesheet':True
                      }

errors = []


pdflatex_cmds = ['pdflatex', '--output-directory=%s' % latex_dir, '--interaction=nonstopmode']
to_latex_cmds   = ['rst2latex.py']

maintmpl = open(os.path.join(TEMPLATE_DIR, 'main.tmpl')).read()
rhs_text = open(os.path.join(TEMPLATE_DIR, 'rhs.tmpl')).read() % {'HTML_ROOT': HTMLROOT}




#name of file that if in a dir will stop bookmaker parsing subdirs
NO_INDEX_SUBDIRS = 'no_index_subdirs'

def setup_chp_dir(chp_dir):
    import warnings
    warnings.warn("setup_chp_dir() is deprecated", DeprecationWarning)

    global chapters_dir
    global SOURCE_RST_ROOT
    global IMG_DIR
    global CSS_DIR
    chapters_dir = chp_dir
    SOURCE_RST_ROOT = chapters_dir



def prepare_config(path_to_meta_dir):
    '''Given a path to the dir holding meta info, set up config as
    needed

    I need the config to be aware of its own location, but I am passing
    in the config to the mkbook script, so I cannot import config as 
    at the import stage for mkbook, it does not exist.

    I thus store config in meta dir of the content folder, then I 
    do a late import ?? Or should I use ConfigParser?


    '''
    pass
