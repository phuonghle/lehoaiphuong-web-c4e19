
# The route must show the calculated BMI AND their condition as following:

# BMI < 16 : Severely underweight
# 16 <= BMI < 18.5: Underweight
# 18.5 <= BMI < 25: Normal
# 25 <= BMI < 30: Overweight
# BMI > 30: Obese

# Do this in 2 ways: With AND without using render_template() function

from flask import Flask, render_template
app = Flask(__name__)
from bmi_cm import bmi_cm


@app.route('/bmi/<int:w>/<int:h>')
# def bmi_rend():
#     return render_template('bmi.html')

def bmi_cmt(w, h):
    bmi = bmi_cm(w, h)
    return bmi

if __name__ == '__main__':
  app.run(debug=True)
 