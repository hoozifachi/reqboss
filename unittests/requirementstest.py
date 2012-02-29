'''
Created on Feb 28, 2012

@author: jason
'''
from elixir import setup_all, metadata, create_all, session, drop_all
from elixir.entity import Entity
from elixir.fields import Field
from model.requirement import Requirement
from sqlalchemy.types import Unicode, Integer, UnicodeText
import unittest


class TestRequirement(unittest.TestCase):


    def setUp(self):
        metadata.bind = 'sqlite:///:memory:'
        create_all()


    def tearDown(self):
        session.close()
        drop_all()


    def testRequirement(self):
        req = Requirement(u'FR', 1, u'New requirement')

        self.assertEqual(u'FR', req.reqtype)
        self.assertEqual(1, req.number)
        self.assertEqual(u'New requirement', req.description)
        
    
    def testQueryRequirement(self):
        req = Requirement(u'FR', 1, u'New requirement')
        
        session.commit()
        
        req1 = Requirement.get_by(number=1)
        
        self.assertEqual(1, req1.number)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()