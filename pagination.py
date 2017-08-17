from app.models import Bucketlist, Item
from flask_restful import fields, marshal
from flask import jsonify, json


# baseq = Item.query.filter()

# page = baseq.paginate(per_page=3)

# while page.has_next or page.page == page.pages:
#     for item in page.items:
#         print("*"*50)
#         print(item.name)
#         print(item.description)
#         print("*"*50)
#     print("End of page {}".format(page.page))
#     page = page.next()

def do_it(page, limit):
    item_fields = {
        'id': fields.Integer,
        'title': fields.String,
        'description': fields.String
    }
    items = Item.query.order_by(Item.id.asc()).paginate(page, limit, error_out=False)
    return json.dumps(marshal(items.items, item_fields))

print(do_it(2, 10))

