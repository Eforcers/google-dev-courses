import webapp2
from models import Person
from datetime import date

class InsertHandler(webapp2.RequestHandler):
    def get(self):
        person = Person(first_name='Pedro',
                        last_name='Perez',
                        email='pedro.perez@mail.com',
                        birth_date=date(1983, 2, 21))
        person.put()
        self.response.write('Inserted Person!')

class ReadHandler(webapp2.RequestHandler):
    def get(self):
        people = Person.query().fetch()
        for person in people:
            self.response.write('First Name: %s <br>'% person.first_name)
            self.response.write('Last Name: %s <br>'% person.last_name)
            self.response.write('email: %s <br>'% person.email)
            self.response.write('birth_date: %s <br>'% person.birth_date)
            self.response.write('age: %s <br>'% person.age)
            self.response.write('<hr>')


class DeleteHandler(webapp2.RequestHandler):
    def get(self):
        people = Person.query().fetch()
        for person in people:
            person.key.delete()
        self.response.write('Deleted Person!')