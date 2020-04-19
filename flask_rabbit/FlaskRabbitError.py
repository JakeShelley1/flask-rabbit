class BaseError(Exception):
  def __init__(self, message, status_code, payload=None):
    self.message = message
    self.payload = payload
    self.status_code = status_code
  
  def __str__(self):
      return str(self.message)

class FailedToAddObjectError(BaseError):
  def __init__(self, message="Failed to add object.", payload=None, status_code=500):
      self.message = message
      self.payload = payload
      self.status_code = status_code

  def __str__(self):
      return str(self.message)

class UnknownError(Exception):
  def __init__(self, message="We're having trouble connecting to the server", payload=None, status_code=500):
      self.message = message
      self.payload = payload
      self.status_code = status_code

  def __str__(self):
      return str(self.message)

class NotFoundError(BaseError):
  def __init__(self, message='Could not find object.', payload=None, status_code=404):
    self.message = message
    self.payload = payload
    self.status_code = status_code
  
  def __str__(self):
      return str(self.message)

class ObjectAlreadyExistsError(BaseError):
  def __init__(self, message='Object could not be inserted because it already exists.', payload=None, status_code=409):
    self.message = message
    self.payload = payload
    self.status_code = status_code
  
  def __str__(self):
      return str(self.message)

class MethodNotAllowedError(BaseError):
  def __init__(self, message='Method not allowed.', status_code=405, payload=None):
    self.message = message
    self.payload = payload
    self.status_code = status_code

  def __str__(self):
    return str(self.message)

class NotAuthorizedError(BaseError):
  def __init__(self, message='Unauthorized.', status_code=401, payload=None):
    self.message = message
    self.payload = payload
    self.status_code = status_code

  def __str__(self):
    return str(self.message)

class InvalidParameterError(BaseError):
  def __init__(self, message='Invalid parameter.', status_code=401, payload=None):
    self.message = message
    self.payload = payload
    self.status_code = status_code

  def __str__(self):
    return str(self.message)