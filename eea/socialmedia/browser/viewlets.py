""" Custom viewlets
"""
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import content
from Products.CMFCore.utils import getToolByName
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

        if pl == "cs":
            new_locale = "cs_CZ"
        elif pl == "da":
            new_locale = "da_DK"
        elif pl == "el":
            new_locale = "el_GR"
        elif pl == "en":
            new_locale = "en_GB"
        elif pl == "et":
            new_locale = "et_EE"
        elif pl == "sl":
            new_locale = "sl_SI"
        elif pl == "sv":
            new_locale = "sv_SE"
        else:
            new_locale = pl + "_" + pl.upper()

        return new_locale





