from models.customer import Customer
import mlab

mlab.connect()

all_customer = Customer.objects()


first_customer = all_customer[0]

# print