from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from collections import Counter
import re
app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     result = ""
#     precision = 2  # default precision
#     if request.method == 'POST':
#         if 'precision' in request.form:
#             precision = int(request.form['precision'])
#
#         length = float(request.form['length'])
#         width = float(request.form['width'])
#         depth = float(request.form['depth'])
#
#         volume = length * width * depth
#         result = round(volume, precision)
#
#     return render_template('home.html', result=result)
@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
     # default precision

    if request.method == 'POST':
        length = float(request.form['length'])
        width = float(request.form['width'])
        depth = float(request.form['depth'])
        if length !=0 and width !=0 and depth !=0:
            if 'precision' in request.form and request.form['precision']:
                precision = int(request.form['precision'])
            else:
                precision = 2  # Установка значения по умолчанию, если precision не был указан или пуст

            volume = length * width * depth
            result = round(volume, precision)

    return render_template('home.html', result=result)
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)