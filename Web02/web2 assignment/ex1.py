# # Continue with the Warm Winter project you have been discussing from Web Session:
# Design a new collection named Customer to save the information (name, gender, email, phone number, job, company, contacted...) 
# of all customers using our service. 
# You can craft the information yourself or fake it using Faker.
# Save the information to the database of Warm Winter project.
# Render the added data in Flask route /customer
# Create a link in home page to show 10 first male, not-yet-contacted customers


from flask import Flask, render_template
import mlab
from models.customer import Customer

app = Flask(__name__)


@app.route('/customer/<g>')
def customer(g):
    all_customer=Customer.objects(
        gender=g,
        contacted=False
    )
    return render_template('customer.html', all_customer=all_customer)

if __name__ == '__main__':
  app.run(debug=True)
 