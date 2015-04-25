from flask import Flask
from flask.ext import restful
from .media import Media_Api, Media_Object_Api
from flask.ext.restful.utils import cors


def create_app(package_name=__name__, settings_override=None, **kwargs):
    app = Flask(package_name, **kwargs)
    app.config.from_object('mediaservice.config.Config')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)
    restapi = restful.Api(app,
                          decorators=[cors.crossdomain(origin='*', methods='*',
                                                       headers='Origin, X-Requested-With, Content-Type, Accept, Options')])
    restapi.add_resource(Media_Api, '/<cmd>', '/', endpoint='media')
    restapi.add_resource(Media_Object_Api,
                         '/o/<sha224hash>/_status',
                         '',
                         endpoint='media')
    return app

