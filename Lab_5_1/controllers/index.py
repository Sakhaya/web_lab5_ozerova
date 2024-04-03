import sys
sys.path.append("..")
import constants

from app import app
from flask import render_template
@app.route('/', methods=['GET'])
def index():
 # выводим форму
 html = render_template('index.html',
                        program_list = constants.programs,
                        subject_list = constants.subjects,
                         len = len)
 return html 
