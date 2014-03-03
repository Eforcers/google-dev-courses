import webapp2
from views import *


app = webapp2.WSGIApplication([
    ('/insert', InsertHandler),
    ('/insert_multi',InsertMultiHandler),
    ('/read_all', ReadAllHandler),
    ('/read', ReadHandler),
    ('/delete', DeleteHandler),
], debug=True)
