from . import MediaserviceApiTest

class Test_Urls(MediaserviceApiTest):

    def test_index(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertEqual(response.json['msg'], "Hello, this is mediaservice")

    def test_media_status(self):
        response = self.client.get('/_status')
        self.assert200(response)
        self.assertIn('msg', response.json)
        self.assertIn('documents', response.json)
        self.assertTrue(response.json['documents'], 1)
        
        

    def test_status(self):
        sha224hash = "2476ac871541a1af54cfd0b04c7363c140870c82e01f2e5c2d641782"
        response = self.client.get('/'+sha224hash+'_status')
        self.assert200(response)
        
