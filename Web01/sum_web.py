from flask import Flask, render_template
app = Flask(__name__)

# import math

@app.route('/sum/<int:x>/<int:y>')
def sum_of(x, y):
    return str(x + y)

if __name__ == '__main__':
  app.run(debug=True)
 