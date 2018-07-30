from models.customer import Customer
import mlab
from faker import Faker
from random import randint, choice


mlab.connect()

fake = Faker()


for i in range(50):
    print("New customer added", i + 1)
    new_customer = Customer(
        name=fake.name(),
        gender=randint(0, 1),
        email=fake.safe_email(),
        phone=fake.phone_number(),
        job=fake.job(),
        company=fake.company(),
        contacted=choice([True, False])
    )
    new_customer.save()

