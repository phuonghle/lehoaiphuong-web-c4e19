from mongoengine import *
import mlab



mlab.connect()


# design database 
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

# new_service = Service(
#     name="Linka",
#     yob=2000,
#     gender=0,
#     height=158,
#     phone="0987345272",
#     address="Hà Nội",
#     status=False
# )


# new_service.save()