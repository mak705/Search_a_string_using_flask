from flask import Flask
from flask import request
from flask import render_template, send_file
import os
import re

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])

def my_form_post():
 text = request.form['text']
 myfile = os.listdir("/some_page/config")
# print myfile
 total_found = []
 for a in myfile:
   a = os.path.join("/some_page/config",a)
   if os.path.isfile(a):
    with open(a, 'r') as f:
     stream = " ".join(f.readlines())
     found = re.findall(text, stream)
     #print a, found
     if found != []:
        val_str = str((a.rsplit('/', 1)[1],found))
        total_found.append(val_str)
 print 'total found ', total_found
 return "\n".join(total_found)

if __name__ == '__main__':
     app.run()