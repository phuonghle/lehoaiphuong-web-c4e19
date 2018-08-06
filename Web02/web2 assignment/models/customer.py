from mongoengine import *
import mlab

mlab.connect()

class Customer(Document):
    # name, gender, email, phone number, job, company, contacted
    name = StringField()
    gender = IntField()
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()

new_customer = Customer(
    name="Linn",
    gender=0,
    email="linn123@gmail.com",
    phone="01234354354",
    job="sales",
    company="IntInt",
    contacted=True

)

new_customer.save()