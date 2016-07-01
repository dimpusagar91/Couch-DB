#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for, render_template
from flask.ext.cors import CORS
from couch import Couch
import json

app = Flask(__name__)
CORS(app)


@app.route('/createdb',methods=['GET', 'POST'])
def createdb():
       foo = Couch('localhost', '5984')
       print "\nCreate database 'mydb':"
       foo.createDb('mydb')

@app.route('/listDB',methods=['GET', 'POST'])
def listDB():
       foo = Couch('localhost', '5984')
       print "\nList databases on server:"
       foo.listDb()

@app.route('/createdoc',methods=['GET', 'POST'])
def createdoc():
       foo = Couch('localhost', '5984')
       print "\nCreate a document 'mydoc' in database 'mydb':"
       doc = """
       {
           "value":
           {
               "Subject":"I like Planktion",
               "Author":"Rusty",
               "PostedDate":"2006-08-15T17:30:12-04:00",
               "Tags":["plankton", "baseball", "decisions"],
               "Body":"I decided today that I don't like baseball. I like plankton."
           }
       }
       """
       foo.saveDoc('mydb', doc, 'mydoc')

@app.route('/createdocwithid',methods=['GET', 'POST'])
def createdocwithid():
       foo = Couch('localhost', '5984')
       print "\nCreate a document, using an assigned docId:"
       doc = """
       {
           "value":
           {
               "Subject":"I like Planktion",
               "Author":"Rusty",
               "PostedDate":"2006-08-15T17:30:12-04:00",
               "Tags":["plankton", "baseball", "decisions"],
               "Body":"I decided today that I don't like baseball. I like plankton."
           }
       }
       """
       foo.saveDoc('mydb', doc)

@app.route('/listalldoc',methods=['GET', 'POST'])
def listalldoc():
       foo = Couch('localhost', '5984')
       print "\nList all documents in database 'mydb'"
       foo.listDoc('mydb')

@app.route('/getDoc',methods=['GET', 'POST'])
def getDoc():
       foo = Couch('localhost', '5984')
       print "\nGet document in database 'mydb' by id"
       foo.getDoc('mydb','mydoc')
       print "\nGet documents in database 'mydb' by keys and values"
       foo.getDoc('mydb',"Author","Rusty")

@app.route('/retrievedoc',methods=['GET', 'POST'])
def retrievedoc():
       foo = Couch('localhost', '5984')
       print "\nRetrieve document 'mydoc' in database 'mydb':"
       foo.openDoc('mydb', 'mydoc')

@app.route('/dbinfo',methods=['GET', 'POST'])
def dbinfo():
       foo = Couch('localhost', '5984')
       print "\nList info about database 'mydb':"
       foo.infoDb('mydb')

@app.route('/deletedb',methods=['GET', 'POST'])
def deletedb():
       foo = Couch('localhost', '5984')
       print "\nDelete database 'mydb':"
       foo.deleteDb('mydb')

@app.route('/deletedoc',methods=['GET', 'POST'])
def deletedoc():
       foo = Couch('localhost', '5984')
       print "\nDelete document 'mydoc' in database 'mydb':"
       foo.deleteDoc('mydb','mydoc')

@app.route('/update',methods=['GET', 'POST'])
def update():
       foo = Couch('localhost', '5984')
       print "\nUpdate document 'mydoc' in database 'mydb':"
       foo.update('mydb', doc, 'mydoc')


if __name__ == '__main__':
    app.run()
