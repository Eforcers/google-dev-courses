from google.appengine.ext import ndb
from datetime import date
import logging

#model
class Person(ndb.Model):
  first_name = ndb.StringProperty(indexed=False)
  last_name = ndb.StringProperty(indexed=False)
  birth_date = ndb.DateProperty(indexed=False)
  email = ndb.StringProperty(indexed=True)

  def calculate_age(self):
    today = date.today()
    return today.year - self.birth_date.year

  age = ndb.ComputedProperty(calculate_age, indexed=False)

class Company(ndb.Model):
    domain = ndb.StringProperty()
    employees_amount = ndb.IntegerProperty(indexed=False)

    def _pre_put_hook(self):
        logging.info('Domain to save [%s]', self.domain)



