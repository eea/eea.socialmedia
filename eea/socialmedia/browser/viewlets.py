""" Custom viewlets
"""
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import content

class SocialMediaViewlet(content.DocumentActionsViewlet):
    """A modified footer viewlet to contain social media icons
    """
    render = ViewPageTemplateFile('socialmedia.pt')
    
        

        
