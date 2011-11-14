""" Layer
"""
import eea.socialmedia
from Products.CMFCore.utils import getToolByName
from transaction import commit
from Products.PloneTestCase.layer import PloneSite
from Testing.ZopeTestCase import app, close, installPackage
from Zope2.App.zcml import load_config
from Products.Five import fiveconfigure as metaconfigure

class SocialMediaLayer(PloneSite):
    """ SocialMediaLayer """

    @classmethod
    def setUp(cls):
        """ setUp """
        root = app()
        portal = root.plone
        # load zcml & install the package
        metaconfigure.debug_mode = True
        load_config('configure.zcml', eea.socialmedia)
        metaconfigure.debug_mode = False
        installPackage('eea.socialmedia', quiet=True)
        # import replacement profile
        profile = 'profile-eea.socialmedia:default'
        tool = getToolByName(portal, 'portal_setup')
        tool.runAllImportStepsFromProfile(profile, purge_old=False)
        # and commit the changes
        commit()
        close(root)

    @classmethod
    def tearDown(cls):
        """ tearDown """
        pass
