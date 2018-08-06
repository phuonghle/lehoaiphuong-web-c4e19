from models.service import Service
import mlab

mlab.connect()

all_service = Service.objects()


first_service = all_service[0]

# find
id_to_find = "5b5b1dc7a86b1c073306104b"

service = Service.objects.with_id(id_to_find)

print(service.to_mongo())

# delete
# if service is not None:
#     service.delete()
#     print("Deleted")
# else:
#     print("Not found")

# update
service.update(set__name="tuan anh", set__yob="2000")
service.reload()
print(service.name)