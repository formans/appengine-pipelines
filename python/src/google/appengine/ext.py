from mock import Mock


blobstore, db, webapp = (Mock() for _ in range(3))

webapp.RequestHandler = object

