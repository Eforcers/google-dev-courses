import webapp2

from views import InsertHandler, InsertMultiHandler, ReadAllHandler, \
    ReadAllKeysHandler, DeleteHandler, DeleteAllHandler, CallHookHandler

app = webapp2.WSGIApplication([
    ('/insert', InsertHandler),
    ('/insert_multi',InsertMultiHandler),
    ('/read_all', ReadAllHandler),
    ('/read', ReadAllHandler),
    ('/read_all_key', ReadAllKeysHandler),
    ('/delete', DeleteHandler),
    ('/delete_all', DeleteAllHandler),
    ('/call_hook', CallHookHandler),
], debug=True)
