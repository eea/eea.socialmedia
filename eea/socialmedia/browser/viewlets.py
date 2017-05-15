""" Custom viewlets
"""
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets import content
from Acquisition import aq_inner

class SocialMediaViewlet(content.DocumentActionsViewlet):
    """A modified footer viewlet to contain social media icons
    """
    render = ViewPageTemplateFile('socialmedia.pt')

    def create_locale(self):
        """There is no way to guess the locale, so we do it by hand.
           Few countries have a different code than their language,
           so we check them case by case
        """
        context = aq_inner(self.context)
        plt = getToolByName(context, 'portal_languages')
        pl = plt.getPreferredLanguage()

        # Social Networks
        locTwitter = pl
        locGoogle = pl
        locFacebook = pl + "_" + pl.upper()

        if pl == "cs":
            locFacebook = "cs_CZ"
        elif pl == "da":
            locFacebook = "da_DK"
        elif pl == "el":
            locFacebook = "el_GR"
        elif pl == "en":
            locGoogle = "en-GB"
            locFacebook = "en_GB"
        elif pl == "et":
            locFacebook = "et_EE"
        elif pl == "pt":
            locGoogle = "pt-PT"
        elif pl == "sl":
            locFacebook = "sl_SI"
        elif pl == "sv":
            locFacebook = "sv_SE"
        elif pl == "zh":
            locGoogle = "zh-CN"

        # Twitter: locales[0]
        # Google plus: locales[1]
        # Facebook: locales[2]
        return (locTwitter, locGoogle, locFacebook)
