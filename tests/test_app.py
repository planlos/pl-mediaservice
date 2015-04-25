from . import MediaserviceApiTest
from flask import Flask


from mediaservice.config import Config, Testing

class Test_App(MediaserviceApiTest):

    def test_appcreation(self):
        self.assertIsNot(self.app, None)
        self.assertIsInstance(self.app, Flask)


    def test_app_config(self):
        #self.assertIsInstance(self.app.config, Testing)
        self.assertTrue(self.app.config['TESTING'])
