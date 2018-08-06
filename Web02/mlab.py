

import mongoengine

# mongodb://<admin>:<admin1234>@ds257241.mlab.com:57241/muadongkhonglanhc4e19

host = "ds257241.mlab.com"
port = 57241
db_name = "muadongkhonglanhc4e19"
user_name = "admin"
password = "admin1234"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())