""" Testing
"""
from  plone.app.testing import PloneSandboxLayer
from  plone.app.testing import applyProfile
from  plone.app.testing import PLONE_FIXTURE
from  plone.app.testing import FunctionalTesting
from zope.configuration import xmlconfig

class EEAFixture(PloneSandboxLayer):
    """ Custom fixture
    """
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """ Setup Zope
        """
        import eea.socialmedia
        xmlconfig.file('configure.zcml',
                       eea.socialmedia,
                       context=configurationContext
                       )

    def setUpPloneSite(self, portal):
        """ Setup Plone
        """
        applyProfile(portal, 'eea.socialmedia:default')

EEAFIXTURE = EEAFixture()
FUNCTIONAL_TESTING = FunctionalTesting(bases=(EEAFIXTURE,),
                                       name='EEASocialMedia:Functional')
