from app import db
from app.models import User, Item, Bucketlist

# user = User("geezluiz", "geezluiz@gmail.com", "qwerty")
for i in range(0, 41):
    # item = Item("Kitu{}".format(i), "description%d" %i, 7)
    bucketlist = Bucketlist('Ndoo{}'.format(i), 'ndoo description %d' %i, 6)
    db.session.add(bucketlist)
    db.session.commit()

db.session.close()