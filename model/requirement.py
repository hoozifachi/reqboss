'''
Created on Feb 28, 2012

@author: jason
'''
from elixir import setup_all
from elixir.entity import Entity
from elixir.fields import Field
from sqlalchemy.types import Unicode, Integer, UnicodeText

class Requirement(Entity):
    reqtype = Field(Unicode(5))
    number = Field(Integer)
    description = Field(UnicodeText)
    
    def __init__(self, reqtype, number, description):
        self.reqtype = reqtype
        self.number = number
        self.description = description
    
setup_all()