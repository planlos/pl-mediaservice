from flask.ext.testing import TestCase
from nose.tools import raises
from mediaservice.api import create_app as app_factory
from mediaservice.config import Testing

class MediaserviceApiTest(TestCase):
    def create_app(self):
        return app_factory(settings_override=Testing())

    def setUp(self):
        pass

    def tearDown(self):
        pass
