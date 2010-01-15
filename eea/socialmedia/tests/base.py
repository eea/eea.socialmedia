from Products.PloneTestCase import PloneTestCase
from Products.GenericSetup import EXTENSION, profile_registry
from eea.socialmedia.tests.layer import SocialMediaLayer
from eea.testcase.base import EEAMegaTestCase
from Products.CMFPlone.interfaces import ITestCasePloneSiteRoot


profile_registry.registerProfile(
                    'testfixture',
                    'test:EEAContentTypes',
                    'Extension profile for testing EEAContentTypes',
                    'profile/testfixture',
                    'EEAContentTypes',
                    EXTENSION,
                    for_=ITestCasePloneSiteRoot)

class FunctionalTestCase(PloneTestCase.FunctionalTestCase):
    pass

class SocialMediaTestCase(FunctionalTestCase):
    layer = SocialMediaLayer

