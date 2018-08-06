from flask import *
# from mongoengine import *
import mlab
from models.service import Service
app = Flask(__name__)

mlab.connect()



@app.route('/')
def index():
    return render_template('index.html')

# @app.routw('/search')
# def search():



@app.route("/search/<g>")
def searching(g):
    all_service = Service.objects(
        gender=g, 
        yob__lte=1998,
        address__exact="Hà Nội"
    )
    return render_template("search.html", all_service=all_service)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service=all_service)

@app.route('/new-service/', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]

    new_service = Service(
        name=name,
        yob=yob,
        phone=phone
    )
    new_service.save()

    return "Name: {}, yob: {}, phone: {}".format(name, yob, phone)


@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_del = Service.objects.with_id(service_id)
    if service_to_del is not None:
        service_to_del.delete()
        return redirect(url_for('admin'))
    else:
        return "Not found"

if __name__ == '__main__':
  app.run(debug=True)
 