import couchdb
from couchdb import *

couch = couchdb.Server('http://127.0.0.1:5984/')
db = couch.create('testing123')
doc = {'foo': 'bar', 'age ': ' 20 ', ' name ' : ' xyz ' }
db.save(doc)
print "document added : ",doc

#Deleting the doc
db.delete(doc)

#Deleting the database
couch.delete('testing123')
