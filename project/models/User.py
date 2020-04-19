from project import db
from sqlalchemy import Column, Integer, BigInteger, Text, ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True)
  name = Column(Text)

  def as_json(self):
    return {
      'id': self.id,
      'name': self.name,
    }
