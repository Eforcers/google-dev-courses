import webapp2
from views import InsertHandler, ReadHandler, DeleteHandler


app = webapp2.WSGIApplication([
    ('/insert', InsertHandler),
    ('/read', ReadHandler),
    ('/delete', DeleteHandler)
], debug=True)
