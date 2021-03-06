from google.appengine.ext import ndb
import webapp2
from models import Person, Company
from datetime import date

class InsertHandler(webapp2.RequestHandler):
    def get(self):
        person = Person(first_name='Pedro',
                        last_name='Perez',
                        email='pedro.perez@mail.com',
                        birth_date=date(1983, 2, 21))
        person.put()
        self.response.write('Inserted Person!')

class InsertMultiHandler(webapp2.RequestHandler):
    def get(self):
        person1 = Person(first_name='Pedro',
                        last_name='Perez',
                        email='pedro.perez@mail.com',
                        birth_date=date(1983, 2, 21))

        person2 = Person(first_name='Juan',
                        last_name='Jimenez',
                        email='juan.jimenez@mail.com',
                        birth_date=date(1985, 4, 28))


        person3 = Person(first_name='Andres',
                        last_name='Acevedo',
                        email='andres.acebedo@mail.com',
                        birth_date=date(1970, 6, 12))

        ndb.put_multi([person1, person2,person3])

        self.response.write('Inserted Person!')

class ReadAllHandler(webapp2.RequestHandler):
    def get(self):
        people = Person.query().fetch()
        for person in people:
            self.response.write('First Name: %s <br>'% person.first_name)
            self.response.write('Last Name: %s <br>'% person.last_name)
            self.response.write('email: %s <br>'% person.email)
            self.response.write('birth_date: %s <br>'% person.birth_date)
            self.response.write('age: %s <br>'% person.age)
            self.response.write('<hr>')

class ReadHandler(webapp2.RequestHandler):
    def get(self):
        people = Person.query(Person.email == 'pedro.perez@mail.com').fetch()
        for person in people:
            self.response.write('First Name: %s <br>'% person.first_name)
            self.response.write('Last Name: %s <br>'% person.last_name)
            self.response.write('email: %s <br>'% person.email)
            self.response.write('birth_date: %s <br>'% person.birth_date)
            self.response.write('age: %s <br>'% person.age)
            self.response.write('<hr>')


class DeleteHandler(webapp2.RequestHandler):
    def get(self):
        person = Person.query(Person.email == 'andres.acebedo@mail.com').fetch()[0]
        person.key.delete()
        self.response.write('Deleted Person!')

class DeleteAllHandler(webapp2.RequestHandler):
    def get(self):
        people = Person.query().fetch(keys_only=True)
        ndb.delete_multi(people)
        self.response.write('Deleted Person!')

class ReadAllKeysHandler(webapp2.RequestHandler):
    def get(self):
        people_keys = Person.query().fetch(keys_only=True)
        for person_key in people_keys:
            self.response.write('kind: %s <br>'% person_key.kind())
            self.response.write('id: %s <br>'% person_key.id())
            self.response.write('urlsafe: %s <br>'% person_key.urlsafe())
            self.response.write('<hr>')

class CallHookHandler(webapp2.RequestHandler):
    def get(self):
        company = Company(domain='mail.com', employees_amount=5)
        company.put()
        self.response.write('Inserted Person!')