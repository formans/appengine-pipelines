from mock import Mock


blobstore, webapp = Mock(), Mock()

webapp.RequestHandler = object

class DB(object):
  mocks = {}
  def __getattr__(self, name):
    if name == 'Model':
      return object
    if name not in self.mocks:
      print 'Mocking db.%s' % (name,)
    return self.mocks.setdefault(name, Mock())


db = DB()
