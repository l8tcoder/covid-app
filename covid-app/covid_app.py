# test change
from flask import Flask
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape
import datetime
import os

myapp = Flask(__name__)
myapp.secret_key = 'aksdlfj203948aksld;fj20934kljsdaf234dlsaf;mna;fjdk02943fakdlsj$%@#_)$%@2='
myapp.config['SECRET_KEY'] = myapp.secret_key
myapp.config['TEMPLATES_AUTO_RELOAD'] = True
myapp.ospath =  os.path.dirname(os.path.realpath(__file__))

templateEnv = myapp.create_jinja_environment()
templateEnv.loader=FileSystemLoader(searchpath="./templates")
templateEnv.line_comment_prefix = "##"
templateEnv.trim_blocks=True
templateEnv.lstrip_blocks=True
templateEnv.autoescape = select_autoescape(['html', 'xml', 'ht', 'htm'])
templateEnv.globals["now"] = datetime.datetime.now
templateEnv.globals["False"] = False
templateEnv.globals["True"] = True

@myapp.route('/')
def covid_start():
    template = templateEnv.get_template('_template1.html')
    page_info = templateEnv.get_template('start_page.ht')
    return template.render({"heading_title": "COVID-19 Incident Tracking", "content": page_info.render()}) 
