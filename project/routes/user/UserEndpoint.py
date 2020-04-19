from project import app, db, models
from flask_rabbit import BaseEndpoint, FlaskRabbitError

class UserEndpoint(BaseEndpoint):
  name = 'user_endpoint'
  url_prefix = '/user'

  def get(self, data):
    models.User.filter_by(name=data['name']).one_or_none()
    return user.as_json()
