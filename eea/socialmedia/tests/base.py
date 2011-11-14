""" Base
"""
from Products.PloneTestCase import PloneTestCase
from eea.socialmedia.tests.layer import SocialMediaLayer


PloneTestCase.setupPloneSite()

class FunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """ FunctionalTestCase """
    pass

class SocialMediaTestCase(FunctionalTestCase):
    """ SocialMediaTestCase """
    layer = SocialMediaLayer
