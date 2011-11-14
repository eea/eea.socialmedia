from Testing import ZopeTestCase
from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase.layer import PloneSite
from transaction import commit


class SocialMediaLayer(PloneSite):

    @classmethod
    def setUp(cls):
        root = ZopeTestCase.app()
        portal = root.plone
        profile = 'profile-eea.socialmedia:default'
        tool = getToolByName(portal, 'portal_setup')
        tool.setImportContext(profile)
        tool.runAllImportSteps()
        commit()
        ZopeTestCase.close(root)

    @classmethod
    def tearDown(cls):
        pass
