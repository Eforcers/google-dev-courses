from google.appengine.ext import ndb
from datetime import date

#model
class Person(ndb.Model):
  first_name = ndb.StringProperty(indexed=False)
  last_name = ndb.StringProperty(indexed=False)
  birth_date = ndb.DateProperty(indexed=False)
  email = ndb.StringProperty()

  def calculate_age(self):
    today = date.today()
    return today.year - self.birth_date.year

  age = ndb.ComputedProperty(calculate_age, indexed=False)