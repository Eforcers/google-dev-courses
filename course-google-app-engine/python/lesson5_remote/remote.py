from models import Person
from google.appengine.ext.remote_api import remote_api_stub

import getpass


def auth_func():
    return raw_input('Username:'), getpass.getpass('Password:')

remote_api_stub.ConfigureRemoteApi(None, '/_ah/remote_api', auth_func,
                                   'remote.www-ecpc.appspot.com')

people = Person.query().fetch()
for person in people:
    print('First Name: %s \n' % person.first_name)
    print('Last Name: %s \n' % person.last_name)
    print('Email: %s \n' % person.email)
    print('Birth date: %s \n' % person.birth_date)
    print('Age: %s \n '% person.age)
    print('-----------')