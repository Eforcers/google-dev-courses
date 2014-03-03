import webapp2
from views import *


app = webapp2.WSGIApplication([
    ('/insert', InsertHandler),
    ('/insert_multi',InsertMultiHandler),
    ('/read_all', ReadAllHandler),
    ('/read', ReadHandler),
    ('/read_all_key', ReadAllKeysHandler),
    ('/delete', DeleteHandler),
    ('/delete_all', DeleteAllHandler),
    ('/call_hook', CallHookHandler),
], debug=True)
