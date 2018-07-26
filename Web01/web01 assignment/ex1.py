# Create a NEW flask app
# Add route “/about-me” (http://127.0.0.1:5000/about-me/) 


# Add route “/school” (http://127.0.0.1:5000/school) so that when users open this route, 
# it automatically redirect them to http://techkids.vn 
# Hint: Google “flask redirect”



from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def about_me():
    return render_template("about_me.html")



@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)
 