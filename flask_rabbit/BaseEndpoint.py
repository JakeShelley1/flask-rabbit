from flask import Flask, request, json, Blueprint
from .FlaskRabbitError import UnknownError, MethodNotAllowedError
import traceback

class BaseEndpoint:
  url_prefix = None
  name = None
  blueprint = None
  
  # Dealing with kwarg url (i.e. <parameter_name>)
  # I'll need to rework this
  has_kwargs = False

  def __init__(self,  app=None, name=None, url_prefix=None):
    if (name != None):
      self.name = name
    if (url_prefix != None):
      self.url_prefix = url_prefix

    assert (name == None), "%s does not have a name assigned." % (self.__class__.__name__)
    assert (url_prefix == None), "%s does not have a url_prefixed." % (self.__class__.__name__)

    self.create_blueprint()

    if (app != None):
      self.register_on(app)

  def register_on(self, app):
    app.register_blueprint(self.blueprint, url_prefix=self.url_prefix)

  def create_blueprint(self):
    self.blueprint = Blueprint(self.name, __name__)
    if (self.has_kwargs):
      self.create_kwargs_router()
    else:
      self.create_router()

  # Methods to implement

  def get(self, data):
    raise MethodNotAllowedError()
  
  def post(self, data):
    raise MethodNotAllowedError()

  def put(self, data):
    raise MethodNotAllowedError()

  def patch(self, data):
    raise MethodNotAllowedError()

  def delete(self, data):
    raise MethodNotAllowedError()

  def create_router(self):
    @self.blueprint.route('/', methods=['POST', 'GET', 'DELETE', 'PATCH', 'PUT'], strict_slashes=False)
    def route():
      Router = {
        'GET': self.get,
        'POST': self.post,
        'PATCH': self.patch,
        'PUT': self.put,
        'DELETE': self.delete,
      }

      try:
        if (request.method not in Router):
          raise MethodNotAllowedError()

        if (request.method == 'GET'):
          return json.dumps(Router[request.method](request.args))

        return json.dumps(Router[request.method](json.loads(request.data)))
      except Exception as e:
        if hasattr(e, 'status_code'):
          return json.dumps({'error':e.__dict__}), e.status_code

        print(traceback.format_exc())
        return json.dumps({'error': UnknownError().__dict__}), 500

  # Methods with kwargs

  def get(self, data, kwargs):
    raise MethodNotAllowedError()
  
  def post(self, data, kwargs):
    raise MethodNotAllowedError()

  def put(self, data, kwargs):
    raise MethodNotAllowedError()

  def patch(self, data, kwargs):
    raise MethodNotAllowedError()

  def delete(self, data, kwargs):
    raise MethodNotAllowedError()


  def create_kwargs_router(self):
    @self.blueprint.route('/', methods=['POST', 'GET', 'DELETE', 'PATCH', 'PUT'], strict_slashes=False)
    def route(**kwargs):
      Router = {
        'GET': self.get,
        'POST': self.post,
        'PATCH': self.patch,
        'PUT': self.put,
        'DELETE': self.delete,
      }

      try:
        if (request.method not in Router):
          raise MethodNotAllowedError()

        if (request.method == 'GET'):
          return json.dumps(Router[request.method](request.args, kwargs))

        return json.dumps(Router[request.method](json.loads(request.data), kwargs))
      except Exception as e:
        if hasattr(e, 'status_code'):
          return json.dumps({'error':e.__dict__}), e.status_code

        print(traceback.format_exc())
        return json.dumps({'error': UnknownError().__dict__}), 500
